from django.contrib import admin
from models import User
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from .resources import UserResource

# Register your models here.

class UserLogin(ImportExportActionModelAdmin, ImportExportModelAdmin,admin.ModelAdmin):
	list_display=['user_id','user_password']
	resource_class = UserResource

admin.site.register(User,UserLogin)

