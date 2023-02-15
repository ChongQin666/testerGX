import datetime

from django.db import models

# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=50)
    addtime = models.DateTimeField(default=datetime.datetime.now())