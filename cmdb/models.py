from django.db import models


# Create your models here.

class UserInfo(models.Model):
    user = models.CharField(max_length=16)
    pwd = models.CharField(max_length=16)


class TestEnv(models.Model):
    url = models.CharField(max_length=200)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    account_xpath = models.CharField(max_length=1000)
    password_xpath = models.CharField(max_length=1000)
    login_button_xpath = models.CharField(max_length=1000)



class TestPoint(models.Model):
    name = models.CharField(max_length=100)
    env_id = models.IntegerField()


class PointStep(models.Model):
    title = models.CharField(max_length=50)
    xpath = models.CharField(max_length=1000)
    action = models.CharField(max_length=20)
    screen = models.CharField(max_length=50)


