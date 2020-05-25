from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Website(models.Model):
    title = models.CharField(max_length=255)
    user = models.CharField(max_length=255,primary_key=True,default="admin")
    description = models.CharField(max_length=255)
    menus = models.CharField(max_length=255, default="yes")
    

    

    def __str__(self):
        return self.title


class Owner(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField()

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
