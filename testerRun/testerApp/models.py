import datetime

from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=50)
    addtime = models.DateTimeField(default=datetime.datetime.now())

class TestItems(models.Model):
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
    SN = models.CharField(max_length=80)

class SNTestLog(models.Model):
    id = models.AutoField(primary_key=True)
    Area = models.CharField(max_length=10)
    Tester = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)
    SN = models.CharField(max_length=80)
    Datetime = models.TimeField(default=timezone.now)
    MAC = models.CharField(max_length=80)
    SAS = models.CharField(max_length=80)
    FileUrl = models.CharField(max_length=100)
    Operation = models.CharField(max_length=50)
    CPU = models.CharField(max_length=50)
    MEM = models.CharField(max_length=50)
    DISK = models.CharField(max_length=50)
    TID = models.CharField(max_length=50)
