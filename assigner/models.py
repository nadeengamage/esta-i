from django.db import models
from simple_history.models import HistoricalRecords
from employee.models import Employee
from department.models import Department


class Assigner(models.Model):
	employee 		= models.ForeignKey(Employee, on_delete=models.CASCADE)
	department 		= models.ForeignKey(Department, on_delete=models.CASCADE)
	working_hours 	= models.TimeField()
	history 		= HistoricalRecords(table_name='assigner_audit_trail')

	# custom save method 
	def save(self, *args, **kwargs):

		# fetching employee details
		try:
		    employee_details = Employee.objects.get(emp_id=self.employee.emp_id, status=1)
		except employee_details.DoesNotExist:
			# if not found the employee then throw the error
			self.employee_not_found_error()
			employee_details = None

		# check employee is active or not
		if employee_details.status is True:
			self.employee_department_validation(employee_details, *args, **kwargs)
		else:
			self.emplpyee_deactivated_error()

			
	# validation befor save emoloyee and department
	def employee_department_validation(self, employee_details, *args, **kwargs):
		try:
			employee_records = self.get_all_objects_by_emp_id(employee_details)
		except Exception as e:
			employee_records = None
		
		if employee_records is not None and employee_records.exists():
			assigned_hours, sum_of_hours = [], None

			for i in range(len(employee_records)):
				assigned_hours.append(str(employee_records[i].get('working_hours')))

			if assigned_hours is not None:
				sum_of_hours = self.get_sum_of_times(assigned_hours)

			if str(employee_details.working_hours) > str(sum_of_hours):
				if str(employee_details.working_hours) >= self.get_sum_of_times([str(sum_of_hours), str(self.working_hours)]):
					super(Assigner, self).save(*args, **kwargs)
				else:
					self.emplpyee_assigned_time_error();	
			else:
				self.emplpyee_assigned_time_error();
		else:
			super(Assigner, self).save(*args, **kwargs)
		
	# get all records from the table
	def get_all_objects_by_emp_id(self, employee_id):
		return Assigner.objects.filter(employee=employee_id).values('working_hours')

	# get assigned total hours by the emolpyee
	def get_sum_of_times(self, time_list):
		total_secs = 0
		for tm in time_list:
		    time_parts = [int(s) for s in tm.split(':')]
		    total_secs += (time_parts[0] * 60 + time_parts[1]) * 60 + time_parts[2]
		total_secs, sec = divmod(total_secs, 60)
		hr, min = divmod(total_secs, 60)
		return ('%02d:%02d:%02d' % (hr, min, sec))

	# throw employee not found error
	def employee_not_found_error(self):
		raise ValueError('Employee not found!')

	# throw employee record not found error
	def employee_record_not_found_error(self):
		raise ValueError('Employee record not found!')

	# throw employee deactivated error
	def emplpyee_deactivated_error(self):
		raise Exception('Employee status is inactivated')

	# throw employee time exceed error
	def emplpyee_assigned_time_error(self):
		raise Exception('Employee cannot assign to depatment due to working hours exceeded!')
		    

	def __str__(self):
		return '{} {} - {}'.format(
			self.employee.first_name, 
			self.employee.last_name, 
			self.department.name
		)

	class Meta(object):
		db_table = 'assigner'
			
		
