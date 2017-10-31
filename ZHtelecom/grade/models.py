# -*- coding=utf-8 -*-
from django.db import models

# Create your models here.
class LeaderGrade(models.Model):
	leader_id=models.CharField(max_length=50)
	mane_id=models.CharField(max_length=50)
	leader_con_grade=models.FloatField()
	leader_beha_grade=models.FloatField()
	leader_gtime=models.DateField(auto_now=True)

class ManagerGrade(models.Model):
	mane_id_active=models.CharField(max_length=50)
	mane_id_passive=models.CharField(max_length=50)
	mane_con_grade=models.FloatField()
	mane_gtime=models.DateField(auto_now=True)

class EmployeeGrade(models.Model):
	emp_id=models.CharField(max_length=50)
	emp_ll_id=models.CharField(max_length=50)
	mane_id=models.CharField(max_length=50)
	emp_beha_grade=models.FloatField()
	emp_gtime=models.DateField(auto_now=True)

