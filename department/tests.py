from django.test import TestCase
from .models import Department

class DepartmentTestCase(TestCase):
	
	def setUp(self):
		Department.objects.create(name='Department1', working_days_per_week='5', working_hours_per_day='08:00:00', status=1)
		Department.objects.create(name='Department2', working_days_per_week='5', working_hours_per_day='09:00:00', status=1)
		Department.objects.create(name='Department3', working_days_per_week='5', working_hours_per_day='09:00:00', status=1)
		Department.objects.create(name='Department4', working_days_per_week='5', working_hours_per_day='08:00:00', status=1)
		Department.objects.create(name='Department5', working_days_per_week='5', working_hours_per_day='09:00:00', status=1)

	def test_department_created(self):
		department1 = Department.objects.get(name='Department1')
		department2 = Department.objects.get(name='Department3')
		department3 = Department.objects.get(name='Department5')

		self.assertEqual(str(department1.working_hours_per_day), '08:00:00')
		self.assertEqual(str(department2.working_hours_per_day), '09:00:00')
		self.assertEqual(str(department3.working_hours_per_day), '09:00:00')
		
