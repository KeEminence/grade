# -*- coding=utf-8 -*-
from django.db import models

# Create your models here.

class User(models.Model):
	user_id=models.CharField(max_length=50)
	user_password=models.CharField(max_length=50)