from django.test import TestCase
from .models import Employee

class EmployeeTestCase(TestCase):
	
	def setUp(self):
		Employee.objects.create(first_name='FName1', last_name='LName1', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName2', last_name='LName2', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName3', last_name='LName3', working_hours='09:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName4', last_name='LName4', working_hours='09:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName5', last_name='LName5', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName6', last_name='LName6', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName7', last_name='LName7', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName8', last_name='LName8', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName9', last_name='LName9', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName10', last_name='LName10', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName11', last_name='LName11', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName12', last_name='LName12', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName13', last_name='LName13', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName14', last_name='LName14', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName15', last_name='LName15', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName16', last_name='LName16', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName17', last_name='LName17', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName18', last_name='LName18', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName19', last_name='LName19', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName20', last_name='LName20', working_hours='08:00:00', date_join='2019-11-15', status=1)

	def test_employee_created(self):
		employee1 = Employee.objects.get(first_name='FName1')
		employee2 = Employee.objects.get(first_name='FName3')
		employee3 = Employee.objects.get(first_name='FName5')

		self.assertEqual(str(employee1.working_hours), '08:00:00')
		self.assertEqual(str(employee2.working_hours), '09:00:00')
		self.assertEqual(str(employee3.working_hours), '08:00:00')
