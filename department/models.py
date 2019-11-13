from django.db import models
from simple_history.models import HistoricalRecords


class Department(models.Model):
	dep_id 					= models.AutoField(primary_key=True)
	name 					= models.CharField(max_length=100)
	working_days_per_week 	= models.IntegerField()
	working_hours_per_day 	= models.TimeField()
	status 					= models.BooleanField('Department active status')
	history					= HistoricalRecords(table_name='department_audit_trail')

	def __str__(self):
		return '{}'.format(self.name)

	class Meta(object):
		db_table = 'department'
			
