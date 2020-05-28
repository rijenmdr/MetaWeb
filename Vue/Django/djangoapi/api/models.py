from django.db import models
from django.conf import settings
from django.utils import timezone


class Website(models.Model):
    nameOfSiteH = models.CharField(max_length=255, default="default")
    headingOneH = models.CharField(max_length=255, default="default")
    descriptionOneH = models.CharField(max_length=255, default="default")
    headingTwoH = models.CharField(max_length=255, default="default")
    descriptionTwoH = models.CharField(max_length=255, default="default")
    headingThreeH = models.CharField(max_length=255, default="default")
    descriptionThreeH = models.CharField(max_length=255, default="default")
    featureOneH = models.CharField(max_length=255, default="default")
    featureTwoH = models.CharField(max_length=255, default="default")
    featureThreeH = models.CharField(max_length=255, default="default")
    introductionA = models.CharField(max_length=255, default="default")
    whatWeDoA = models.CharField(max_length=255, default="default")
    titleC = models.CharField(max_length=255, default="default")
    emailC = models.CharField(max_length=255, default="default")
    descriptionC = models.CharField(max_length=255, default="default")
    phoneC = models.CharField(max_length=255, default="default")
    addressC = models.CharField(max_length=255, default="default")
    user = models.CharField(max_length=255, default="default")
    created_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.user
