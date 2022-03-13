from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    files = models.FileField(verbose_name='Attachment(File)', upload_to='documents/%Y/%m/%d')
    images = models.ImageField(verbose_name='Attachment(Image)', upload_to='documents/%Y/%m/%d', width_field=None, height_field=None)

    def __str__(self):
        return self.title
    