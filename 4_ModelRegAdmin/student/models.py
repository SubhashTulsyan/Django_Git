from django.db import models

# Create your models here.
class Student(models.Model):
    branches = (
        ('-1', '--Select--'),
        ('CS', 'Computer Science'),
        ('ME', 'Mechanical Engineering'),
    )
    roll = models.IntegerField()
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100, choices=branches, default='-1')

    def __str__(self):
        return str(self.pk)+' '+self.name
    