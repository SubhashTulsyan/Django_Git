from django.db import models
from datetime import datetime
# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    date = models.DateTimeField(default=datetime.today())
    class Meta:
        abstract = True

class Student(CommonInfo):
    roll = models.IntegerField()
    date = models.DateField()

class Teacher(CommonInfo):
    emp_id = models.IntegerField()
    date = None