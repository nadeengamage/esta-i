from django.db import models
from simple_history.models import HistoricalRecords
from employee.models import Employee
from department.models import Department


class Assigner(models.Model):
	employee 		= models.ForeignKey(Employee, on_delete=models.CASCADE)
	department 		= models.ForeignKey(Department, on_delete=models.CASCADE)
	working_hours 	= models.TimeField()
	history 		= HistoricalRecords(table_name='assigner_audit_trail')

	def __str__(self):
		return '{} - {}'.format(
			self.employee.first_name, 
			self.employee.last_name, 
			self.department.name
		)

	class Meta(object):
		db_table = 'assigner'
			
		
