# -*- coding=utf-8 -*-
from django.db import models

# Create your models here.

class User(models.Model):
	user_id=models.CharField(max_length=50,primary_key=True)
	user_password=models.CharField(max_length=50)
	def __str__(self):
		return self.user_id.encode('utf-8')

