from django.contrib import admin

# Register your models here.
from django.contrib import  admin
from .models import *

admin.site.register(User)
admin.site.register(HealthInfo)
# 超级管理员用户密码
# admin  qwe123456

# 登录http://127.0.0.1:8000/app/login/