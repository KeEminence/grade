from django.contrib import admin
from blog.models import Blog
from models import User

# Register your models here.

admin.site.register(User)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display=('id','user_id','user_password')