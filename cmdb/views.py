import json

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from cmdb import models
from django.contrib import messages


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


def case_list(request, nid):
    row_data = models.TestPoint.objects.filter(env_id=nid).all()
    env_name = models.TestEnv.objects.filter(id=nid).first()
    return render(request, 'case_list.html', {"case_data": row_data, "env": env_name})


def case_add(request, nid):
    if request.method == "GET":
        return render(request, 'case_add.html', {"env_id": nid})
    name = request.POST.get("case_name")
    models.TestPoint.objects.create(name=name, env_id=nid)
    return redirect("/case/%s/list" % str(nid))


def delete_case(request):
    nid = request.GET.get('nid')
    env_id = request.GET.get("env_id")
    models.TestPoint.objects.filter(id=nid).delete()
    return redirect("/case/%s/list" % str(env_id))


def case_edit(request, nid):
    if request.method == "GET":
        row_data = models.TestPoint.objects.filter(id=nid).first()
        env_id = request.GET.get("env_id")
        print(env_id)
        return render(request, 'case_edit.html', {"row_data": row_data,"env_id": env_id})
    env_id = request.GET.get("env_id")
    name = request.POST.get("name")
    models.TestPoint.objects.filter(id=nid).update(name=name)
    return redirect("/case/%s/list" % str(env_id))

def step_list(request, nid):
    row_data = models.PointStep.objects.filter(point_id=nid).all()
    point_name = models.TestPoint.objects.filter(id=nid).first()
    return render(request, 'step_list.html', {"case_data": row_data, "env": point_name})
