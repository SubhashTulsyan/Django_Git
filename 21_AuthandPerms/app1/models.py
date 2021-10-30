from django.db import models

# Create your models here.
class blog(models.Model):
    name = models.CharField(max_length=80)
    title = models.CharField(max_length=10)