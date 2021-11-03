from django.db import models

# Create your models here.
class FatherModel(models.Model):
    father_name = models.CharField(max_length=80)

class SonModel(FatherModel):
    son_name = models.CharField(max_length=80)

class DaughterModel(FatherModel):
    daughter_name = models.CharField(max_length=80)