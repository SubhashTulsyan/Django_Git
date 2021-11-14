from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=100)
    duration = models.TimeField()
    singer = models.ManyToManyField(User)

    def sung_by(self):
        return ', '.join([str(i) for i in self.singer.all()])    
