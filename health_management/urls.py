"""health_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin #这行代码导入Django的管理后台模块
from django.urls import path,include
#这行代码导入了 Django 的 URL 相关模块，其中path用于定义 URL 路由，include用于包含其他应用的 URL 配置。
from django.conf import settings#导入了Django项目的设置模块
from django.conf.urls.static import static#静态文件配置相关模块

urlpatterns = [
    path('admin/', admin.site.urls),#admin.site.urls是管理后台的URL配置
    path('app/',include('app.urls'))#通过include('app.urls')引入该应用程序下的 URL 配置。
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# 设置登录页
admin.site.site_title = '健康睡眠数据系统后台'
admin.site.site_header = '健康睡眠数据系统后台'
