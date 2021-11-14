from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    password = models.CharField(max_length=10)