from django.contrib import admin
from models import LeaderGrade,ManagerGrade,EmployeeGrade
# Register your models here.

admin.site.register(LeaderGrade)
admin.site.register(ManagerGrade)
admin.site.register(EmployeeGrade)