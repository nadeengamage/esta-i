from django.db import models
from employee.models import Employee
from department.models import Department
from django.core.validators import ValidationError


class Assigner(models.Model):
	id 				= models.AutoField(primary_key=True)
	employee 		= models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_id')
	department 		= models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dep_id')
	working_hours 	= models.TimeField()

	# validate working hours of the employee
	def validate_unique(self, *args, **kwargs):
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
					pass
				else:
					self.emplpyee_assigned_time_error();	
			else:
				self.emplpyee_assigned_time_error();
		
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
		raise ValidationError({'working_hours': 'Employee cannot assign to depatment due to working hours exceeded!'})
		super(Assigner, self).validate_unique(*args, **kwargs)

	def save(self, *args, **kwargs):
		if self.id is None:	
			super(Assigner, self).save(*args, **kwargs)
			assigner = Assigner.objects.get(id=self.id)
			self.history(assigner, 'Inserted Record', 'CREATED')
		else:
			super(Assigner,self).save(*args, **kwargs)
			assigner = Assigner.objects.get(id=self.id)
			self.history(assigner, 'Updated Record', 'UPDATED')

	def delete(self, *args, **kwargs):
		super(Assigner, self).delete(*args, **kwargs)
		assigner = Assigner.objects.get(id=self.id)
		self.history(assigner, 'Deleted Record', 'DELETED')

	def history(self, model, history_change_reason, history_type):
		AssignerHistory.objects.create(
			assigner = model,
			employee = Employee.objects.get(emp_id=model.employee.emp_id),
			department = Department.objects.get(dep_id=model.department.dep_id),
			working_hours = self.working_hours,
			history_change_reason = history_change_reason,
			history_type = history_type
		)

	def __str__(self):
		return '{} {} - {}'.format(
			self.employee.first_name, 
			self.employee.last_name, 
			self.department.name
		)

	class Meta(object):
		db_table = 'assigner'
			
		

class AssignerHistory(models.Model):
	history_id 				= models.AutoField(primary_key=True)
	assigner 				= models.ForeignKey(Assigner, on_delete=models.CASCADE)
	employee 				= models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_id')
	department 				= models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dep_id')
	working_hours 			= models.TimeField()
	history_change_reason 	= models.CharField(max_length=50)
	history_type 			= models.CharField(max_length=10)
	history_date 			= models.DateTimeField(auto_now_add=True)
	
	class Meta(object):
		db_table = 'assigner_audit_trail'
		