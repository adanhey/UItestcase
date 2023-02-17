import json

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from cmdb import models


# Create your views here.


def index(request):
    case_list = models.TestEnv.objects.all()
    return render(request, "index.html", {"data": case_list})


def add_env(request):
    if request.method == "GET":
        return render(request, 'environment_add.html')
    name = request.POST.get("name")
    url = request.POST.get("url")
    account = request.POST.get("account")
    password = request.POST.get("password")
    account_xpath = request.POST.get("account_xpath")
    password_xpath = request.POST.get("password_xpath")
    login_button_xpath = request.POST.get("login_xpath")
    models.TestEnv.objects.create(name=name, url=url, account=account, password=password, account_xpath=account_xpath,
                                  password_xpath=password_xpath, login_button_xpath=login_button_xpath)
    return redirect("/index/")


def delete_env(request):
    nid = request.GET.get('nid')
    models.TestEnv.objects.filter(id=nid).delete()
    user_list = models.TestEnv.objects.all()
    return redirect("/index/")


def edit_env(request, nid):
    if request.method == "GET":
        row_data = models.TestEnv.objects.filter(id=nid).first()
        return render(request, 'environment_edit.html', {"row_data": row_data})
    name = request.POST.get("name")
    url = request.POST.get("url")
    account = request.POST.get("account")
    password = request.POST.get("password")
    account_xpath = request.POST.get("account_xpath")
    password_xpath = request.POST.get("password_xpath")
    login_button_xpath = request.POST.get("login_xpath")
    models.TestEnv.objects.filter(id=nid).update(name=name, url=url, account=account, password=password,
                                                 account_xpath=account_xpath, password_xpath=password_xpath,
                                                 login_button_xpath=login_button_xpath)
    return redirect("/index/")
