import json

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from cmdb import models


# Create your views here.


def index(request):
    # return HttpResponse("hello world!")
    if request.method == "POST":
        url = request.POST.get("url", None)
        account = request.POST.get("account", None)
        password = request.POST.get("password", None)
        account_xpath = request.POST.get("account_xpath", None)
        password_xpath = request.POST.get("password_xpath", None)
        login_button_xpath = request.POST.get("login_button_xpath", None)
        # username = request.POST.get("username", None)
        # password = request.POST.get("password", None)
        models.TestEnv.objects.create(
            url=url,
            account=account,
            password=password,
            account_xpath=account_xpath,
            password_xpath=password_xpath,
            login_button_xpath=login_button_xpath,
        )
    user_list = models.TestEnv.objects.all()
    return render(request, "index.html", {"data": user_list})


def delete_env(request, del_id):
    models.TestEnv.objects.filter(id=del_id).delete()
    user_list = models.TestEnv.objects.all()
    return redirect('http://192.168.3.2:8000/index/')


def edit_env(request, edit_id):
    if request.method == "POST":
        edit_id = request.POST.get("edit_id", None)
        url = request.POST.get("edit_url", None)
        account = request.POST.get("edit_account", None)
        password = request.POST.get("edit_password", None)
        account_xpath = request.POST.get("edit_account_xpath", None)
        password_xpath = request.POST.get("edit_password_xpath", None)
        login_button_xpath = request.POST.get("edit_login_button_xpath", None)
        models.TestEnv.objects.filter(id=edit_id).update(
            url=url,
            account=account,
            password=password,
            account_xpath=account_xpath,
            password_xpath=password_xpath,
            login_button_xpath=login_button_xpath,
        )
        user_list = models.TestEnv.objects.all()
        return render(request, "index.html", {"data": user_list})
