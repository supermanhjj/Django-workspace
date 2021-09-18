"""digital_retina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
# vue add
from django.views.generic.base import TemplateView
# import digital_retina_system.urls
# vue add

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# vue modify
# 使用Django的通用视图TemplateView修改静态指向路径
# 就是让Django访问目录指向我们刚才打包的dist/index.html
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('digital_retina_system.urls')),
    path('',TemplateView.as_view(template_name="index.html")),
]
# vue modify
