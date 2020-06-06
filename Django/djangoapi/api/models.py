from django.db import models
from django.conf import settings
from django.utils import timezone


class Website(models.Model):
    nameOfSiteH = models.CharField(max_length=255, default="NameOfSite")
    category = models.CharField(max_length=255, default="category")
    headingOneH = models.CharField(max_length=255, default="heading One")
    descriptionOneH = models.CharField(
        max_length=255, default="description one")
    headingTwoH = models.CharField(max_length=255, default="Heading Two")
    descriptionTwoH = models.CharField(
        max_length=255, default="description two")
    headingThreeH = models.CharField(max_length=255, default="heading three")
    descriptionThreeH = models.CharField(
        max_length=255, default="description three")
    featureOneH = models.CharField(max_length=255, default="feature One")
    featureOneDesH = models.CharField(
        max_length=255, default="feature description one")
    featureTwoH = models.CharField(max_length=255, default="feature Two")
    featureTwoDesH = models.CharField(
        max_length=255, default="feature description two")
    featureThreeH = models.CharField(max_length=255, default="feature three")
    featureThreeDesH = models.CharField(
        max_length=255, default="feature description three")
    introductionA = models.CharField(max_length=255, default="introduction")
    whatWeDoA = models.CharField(max_length=255, default="what we do")
    titleC = models.CharField(max_length=255, default="title")
    emailC = models.EmailField(max_length=255)
    descriptionC = models.CharField(max_length=255, default="description")
    phoneC = models.CharField(max_length=255)
    addressC = models.CharField(max_length=255, default="address")
    serviceOne = models.CharField(max_length=255, default="Service One")
    serviceOneDes = models.CharField(
        max_length=255, default="description of service one")
    serviceTwo = models.CharField(max_length=255, default="Service Two")
    serviceTwoDes = models.CharField(
        max_length=255, default="description of service two")
    serviceThree = models.CharField(max_length=255, default="Service Three")
    serviceThreeDes = models.CharField(
        max_length=255, default="description of service three")
    backgroundColor = models.CharField(
        max_length=255, default="backgroundColor")
    user = models.CharField(max_length=255, default="user")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user


class Hotel(models.Model):
    user = models.CharField(max_length=255, default="user")
    name = models.CharField(max_length=255, default="name")
    category = models.CharField(max_length=255, default="category")
    welcomeOne = models.CharField(max_length=255, default="welcomeOne")
    welcomeOneDes = models.CharField(max_length=255, default="welcomeOneDes")
    welcomeOneDes = models.CharField(max_length=255, default="welcomeTwo")
    welcomeTwoDes = models.CharField(max_length=255, default="welcomeTwoDes")
    about = models.CharField(max_length=555, default="about")
    galleryDes = models.CharField(max_length=255, default="galleryDes")
    phone = models.CharField(max_length=255, default="phone")

    email = models.EmailField(max_length=255, default='admin@admin.com')
    location = models.CharField(max_length=255, default="location")
    aboutFooter = models.CharField(max_length=255, default="aboutFooter")
    openingHours = models.CharField(max_length=255, default="openingHours")
    fbLink = models.CharField(max_length=255, default="fbLink")
    instaLink = models.CharField(max_length=255, default="instaLink")
    youtubeLink = models.CharField(max_length=255, default="youtubeLink")
    backgroundColor = models.CharField(
        max_length=255, default="backgroundColor")
    photo_1 = models.ImageField(upload_to="%y/%m/%d", default='')
    photo_2 = models.ImageField(upload_to="%y/%m/%d", default='')
    photo_3 = models.ImageField(upload_to="%y/%m/%d", default='')
    photo_4 = models.ImageField(upload_to="%y/%m/%d", default='')
    photo_5 = models.ImageField(upload_to="%y/%m/%d", default='')
    photo_6 = models.ImageField(upload_to="%y/%m/%d", default='')
    photo_7 = models.ImageField(upload_to="%y/%m/%d", default='')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user


class Visitor(models.Model):
    user = models.ForeignKey(Website, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    shopId = models.IntegerField()

    def __str__(self):
        return self.first_name


class MetaWebFeedback(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.email


class PaidUser(models.Model):

    username = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
