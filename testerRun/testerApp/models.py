import datetime

from django.db import models

# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=50)
    addtime = models.DateTimeField(default=datetime.datetime.now())

class testItems(models.Model):
    id = models.AutoField(primary_key=True)
    cpu = models.BooleanField(blank=True)
    mem = models.BooleanField(blank=True)
    fan = models.BooleanField(blank=True)
    hdd = models.BooleanField(blank=True)
    pcie = models.BooleanField(blank=True)
    bios = models.BooleanField(blank=True)
    disk = models.BooleanField(blank=True)
    fru = models.BooleanField(blank=True)
    sdd = models.BooleanField(blank=True)
    usb = models.BooleanField(blank=True)
    id_light = models.BooleanField(blank=True)


