from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Assigner


def index(request):
	assigner_list = Assigner.objects.all()
	paginator = Paginator(assigner_list, 10)

	page = request.GET.get('page')
	assigners = paginator.get_page(page)

	return render(request, 'assigner/views/index.html', {'assigners': assigners})
