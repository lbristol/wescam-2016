from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    isRegistered = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True)
    email = models.CharField(max_length=40, blank=True,null=True)
    gender = models.CharField(max_length=40, blank=True,null=True)
    year = models.IntegerField()
    lastName = models.CharField(max_length=40, blank=True,null=True)
    firstName = models.CharField(max_length=40, blank=True,null=True)

class Crush(models.Model):
    crusher = models.ForeignKey(User, related_name="crusher")
    crushee = models.ForeignKey(User, related_name="crushee")
    reciprocated = models.BooleanField()
    nickname = models.CharField(max_length=40, blank=True,null=True)
