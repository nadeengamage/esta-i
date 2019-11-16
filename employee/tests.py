from django.test import TestCase
from .models import Employee

class EmployeeTestCase(TestCase):
	
	def setUp(self):
		Employee.objects.create(first_name='FName1', last_name='LName1', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName2', last_name='LName2', working_hours='08:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName3', last_name='LName3', working_hours='09:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName4', last_name='LName4', working_hours='09:00:00', date_join='2019-11-15', status=1)
		Employee.objects.create(first_name='FName5', last_name='LName5', working_hours='08:00:00', date_join='2019-11-15', status=1)

	def test_employee_created(self):
		employee1 = Employee.objects.get(first_name='FName1')
		employee2 = Employee.objects.get(first_name='FName3')
		employee3 = Employee.objects.get(first_name='FName5')

		self.assertEqual(str(employee1.working_hours), '08:00:00')
		self.assertEqual(str(employee2.working_hours), '09:00:00')
		self.assertEqual(str(employee3.working_hours), '08:00:00')
