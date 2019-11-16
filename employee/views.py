from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Employee


def index(request):
	employee_list = Employee.objects.all()
	paginator = Paginator(employee_list, 10)

	page = request.GET.get('page')
	employees = paginator.get_page(page)

	return render(request, 'employee/views/index.html', {'employees': employees})
