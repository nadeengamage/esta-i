from django.db import models
from simple_history.models import HistoricalRecords


class Employee(models.Model):
	emp_id 			= models.AutoField(primary_key=True)
	first_name 		= models.CharField(max_length=50)
	last_name 		= models.CharField(max_length=50)
	working_hours	= models.TimeField(auto_now=False, auto_now_add=False)
	date_join 		= models.DateField()
	date_left 		= models.DateField('Left Date',auto_now=False, auto_now_add=False, null=True, blank=True)
	status 			= models.BooleanField('Employee Active Status') # if status is 1 then employee is active in the organization.
	history 		= HistoricalRecords(table_name='employee_audit_trail')

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)

	class Meta(object):
		db_table = 'employee'


