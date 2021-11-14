from django.db import models
from django.contrib.auth.models import User
#from datetime import date
# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publishDate = models.DateField()
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publishDate = models.DateField()

class Song(models.Model):
    singer = models.ManyToManyField(User, related_name='singer_id')
    name = models.CharField(max_length=100)
    duration = models.DurationField()

    def sung_by(self):
        return ', '.join([str(i) for i in self.singer.all()])