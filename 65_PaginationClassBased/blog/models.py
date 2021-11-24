from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    post = models.TextField(max_length=2000)
    pub_date = models.DateField()
    
    def __str__(self):
        return self.title
    
