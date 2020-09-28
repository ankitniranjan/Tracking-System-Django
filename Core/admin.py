from django.contrib import admin
from .models import User, ActiveUser
# Register your models here.

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'email', 'phone', 'reg_no']

@admin.register(ActiveUser)
class ActiveUserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'registered_id' ,'fullname', 'reg_no', 'location', 'speed', 'time']