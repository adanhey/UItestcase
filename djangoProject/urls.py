"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import re_path
from cmdb import views

urlpatterns = [
    # path('front_page/', templates.depart.edit.html),
    path('environment/add/', views.add_env),
    path('index/', views.index),
    path('environment/delete/', views.delete_env),
    path('case/delete/', views.delete_case),
    re_path('^environment/(\d+)/edit/', views.edit_env),
    re_path('^case/(\d+)/edit/', views.case_edit),
    re_path('^case/(\d+)/list/', views.case_list),
    re_path('^case/(\d+)/add/', views.case_add),
    re_path('^step/(\d+)/list/', views.step_list),
    # re_path('^index/delete_env/(\d+)', views.delete_env),
    # re_path('edit_env/', views.edit_env),
]
