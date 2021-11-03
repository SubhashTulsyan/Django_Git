from django.db import models
from datetime import datetime
# Create your models here.
class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=80)
    roll = models.IntegerField(unique=True, blank=False)
    pass_date = models.DateField()
    created_datetime = models.DateTimeField(null=False, default=datetime.now())
class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=80)
    roll = models.IntegerField(unique=True, blank=False)