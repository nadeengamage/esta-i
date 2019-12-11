import uuid
from django.db import models

class Department(models.Model):
	dep_id 					= models.AutoField(primary_key=True)
	identity_no				= models.UUIDField(default=uuid.uuid4, editable=False)
	name 					= models.CharField(max_length=100)
	working_days_per_week 	= models.IntegerField()
	working_hours_per_day 	= models.TimeField()
	status 					= models.BooleanField('Department active status')

	def save(self, *args, **kwargs):
		if self.dep_id is None:	
			super(Department, self).save(*args, **kwargs)
			department = Department.objects.get(dep_id=self.dep_id)
			self.history(department, 'Inserted Record', 'CREATED')
		else:
			super(Department,self).save(*args, **kwargs)
			department = Department.objects.get(dep_id=self.dep_id)
			self.history(department, 'Updated Record', 'UPDATED')

	def delete(self, *args, **kwargs):
		super(Department, self).delete(*args, **kwargs)
		department = Department.objects.get(dep_id=self.dep_id)
		self.history(department, 'Deleted Record', 'DELETED')

	def history(self, model, history_change_reason, history_type):
		DepartmentHistory.objects.create(
			department 				= model,
			name 					= self.name,
			working_days_per_week 	= self.working_days_per_week,
			working_hours_per_day 	= self.working_hours_per_day,
			status 					= self.status,
			history_change_reason 	= history_change_reason,
			history_type 			= history_type
		)

	def __str__(self):
		return '{}'.format(self.name)

	class Meta(object):
		db_table = 'department'

			
class DepartmentHistory(models.Model):
	history_id 				= models.AutoField(primary_key=True)
	department 				= models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dep_id')
	name 					= models.CharField(max_length=100)
	working_days_per_week 	= models.IntegerField()
	working_hours_per_day 	= models.TimeField()
	status 					= models.BooleanField()
	history_change_reason 	= models.CharField(max_length=50)
	history_type 			= models.CharField(max_length=10)
	history_date 			= models.DateTimeField(auto_now_add=True)

	class Meta(object):
		db_table = 'department_audit_trail'
