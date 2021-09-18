"""myDjango URL Configuration

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

from myDemoApp1 import views, views_testdb, search_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('test/', views.test),
    path('testdb/', views_testdb.testdb),
    path('search-post/', search_post.search_post),
    # path('login/', views.login, name='login'),
    path('add_book/', views.add_book),
    path('search_book/', views.search_book),
    path('add_emp/', views.add_emp),
    path('login/', views.login),
    path('index/', views.index),
    path('logout/', views.logout),
    path('order/', views.logout)
]
