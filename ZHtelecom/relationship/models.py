from django.db import models

# Create your models here.
class Leader(models.Model):
	leader_id=models.CharField(max_length=50)
	leader_name=models.CharField(max_length=50)

class Manager(models.Model):
	mane_id=models.CharField(max_length=50)
	mane_name=models.CharField(max_length=50)
	mane_level=models.CharField(max_length=50)
	mane_dept=models.CharField(max_length=50)

class Employee(models.Model):
	emp_id=models.CharField(max_length=50)
	emp_name=models.CharField(max_length=50)
	emp_dept=models.CharField(max_length=50)
	