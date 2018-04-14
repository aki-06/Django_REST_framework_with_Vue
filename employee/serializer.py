from rest_framework import serializers
from employee.model import Employee


class EmployeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Employee
		fields = ("id", "name", "age", "department")