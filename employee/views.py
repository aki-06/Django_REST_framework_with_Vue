import os

from django.conf import settings
from django.http.response import HttpResponse
from rest_framework import viewsets

from employee.models import Employee
from employee.serializer import EmployeeSerializer

def index(_):
	"""静的ファイルを返すview"""
	html = open(os.path.join(settings.STATICFILES_DIRS[0], "vue_grid.html")).read()
	return HttpResponse(html)


class EmployeeViewSet(viewsets.ModelViewSet):
	"""RestAPIのviewsets"""
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	filter_fields = ("id", "name", "age", "department")