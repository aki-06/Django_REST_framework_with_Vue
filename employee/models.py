from django.db import models


class Employee(models.Model):

	class Meta:
		db_table = 'employee'
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	age = models.IntegerField()
	department = models.CharField(max_length=255)
