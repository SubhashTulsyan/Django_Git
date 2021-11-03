from django.db import models
from django.db.models.query_utils import Q

# Create your models here.
class StudentOrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-id')
    def notEqualManager(self, id):
        return super().get_queryset().filter(~Q(id=id))

class Student(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    #students  = StudentOrderManager()
    #objects = models.Manager()

class StudentProxy(Student):
    students  = StudentOrderManager()
    class Meta:
        proxy = True
        ordering = ['name']

