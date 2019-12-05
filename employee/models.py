from django.db import models


class Employee(models.Model):
	emp_id 			= models.AutoField(primary_key=True)
	first_name 		= models.CharField(max_length=50)
	last_name 		= models.CharField(max_length=50)
	working_hours	= models.TimeField(auto_now=False, auto_now_add=False)
	date_join 		= models.DateField()
	date_left 		= models.DateField('Left Date',auto_now=False, auto_now_add=False, null=True, blank=True)
	status 			= models.BooleanField('Employee Active Status') # if status is 1 then employee is active in the organization.

	def save(self, *args, **kwargs):
		if self.emp_id is None:	
			super(Employee, self).save(*args, **kwargs)
			employee = Employee.objects.get(emp_id=self.emp_id)
			self.history(employee, 'Inserted Record', 'CREATED')
		else:
			super(Employee,self).save(*args, **kwargs)
			employee = Employee.objects.get(emp_id=self.emp_id)
			self.history(employee, 'Updated Record', 'UPDATED')

	def delete(self, *args, **kwargs):
		super(Employee, self).delete(*args, **kwargs)
		employee = Employee.objects.get(emp_id=self.emp_id)
		self.history(employee, 'Deleted Record', 'DELETED')

	def history(self, model, history_change_reason, history_type):
		EmployeeHistory.objects.create(
			employee = model,
			first_name = self.first_name,
			last_name = self.last_name,
			working_hours = self.working_hours,
			date_join = self.date_join,
			date_left = self.date_left,
			status = self.status,
			history_change_reason = history_change_reason,
			history_type = history_type
		)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)

	class Meta(object):
		db_table = 'employee'

class EmployeeHistory(models.Model):
	history_id 				= models.AutoField(primary_key=True)
	employee 				= models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_id')
	first_name 				= models.CharField(max_length=50)
	last_name 				= models.CharField(max_length=50)
	working_hours			= models.TimeField()
	date_join 				= models.DateField()
	date_left 				= models.DateField(null=True, blank=True)
	status 					= models.BooleanField()
	history_change_reason 	= models.CharField(max_length=50)
	history_type 			= models.CharField(max_length=10)
	history_date 			= models.DateTimeField(auto_now_add=True)

	class Meta(object):
		db_table = 'employee_audit_trail'


