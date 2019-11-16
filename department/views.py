from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Department

def index(request):
	department_list = Department.objects.all()
	paginator = Paginator(department_list, 10)

	page = request.GET.get('page')
	departments = paginator.get_page(page)

	return render(request, 'department/views/index.html', {'departments': departments})
