from django.db import models
from django.contrib.auth.models import User
from User.models import *




class Dobro(models.Model):
    # author = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    investment = models.IntegerField(null=True)
    comments = models.TextField(null=True, blank=True)
