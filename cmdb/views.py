from django.shortcuts import render
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
