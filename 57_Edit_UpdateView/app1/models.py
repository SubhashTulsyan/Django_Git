from django.db import models
from django.urls import reverse
class Student(models.Model):
    name = models.CharField(max_length=80)
    roll = models.IntegerField()
    doj = models.DateField()
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={'pk': self.pk})
    