from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50, help_text='Namemm')
    roll = models.IntegerField()
    email = models.EmailField(
        blank=True,
        #verbose_name='EMAIL',
        #help_text='HelpEmail'
        )
    password = models.CharField(max_length=10, default='a')