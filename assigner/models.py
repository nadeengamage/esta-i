from django.db import models
from simple_history.models import HistoricalRecords
from employee.models import Employee
from department.models import Department
import sys


class Assigner(models.Model):
	employee 		= models.ForeignKey(Employee, on_delete=models.CASCADE)
	department 		= models.ForeignKey(Department, on_delete=models.CASCADE)
	working_hours 	= models.TimeField()
	history 		= HistoricalRecords(table_name='assigner_audit_trail')

	def save(self, *args, **kwargs):
		
		try:
		    employee_details = Employee.objects.get(emp_id=self.employee.emp_id)
		except employee_details.DoesNotExist:
			self.employee_not_found_error()
			employee_details = None

		try:
			employee_records = self.get_all_objects_by_emp_id(employee_details)
		except Exception as e:
			employee_records = None

		print(count(employee_records), file=sys.stderr)

		# if employee_records is None:
		# super(Assigner, self).save(*args, **kwargs)
			# pass
		# sum = datetime.timedelta()
		# for i in timeList:
		#     (h, m, s) = i.split(':')
		#     d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
		#     sum += d
		# print(str(sum))

	def get_all_objects_by_emp_id(self, employee_id):
		return self._meta.model.objects.get(employee=employee_id)

	def employee_not_found_error(self):
		raise ValueError('Employee not found!')

	def employee_record_not_found_error(self):
		raise ValueError('Employee record not found!')
		    

	def __str__(self):
		return '{} {} - {}'.format(
			self.employee.first_name, 
			self.employee.last_name, 
			self.department.name
		)

	class Meta(object):
		db_table = 'assigner'
			
		
