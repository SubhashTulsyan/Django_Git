from django.db import models
from django.contrib.auth.models import User
from datetime import date
class Post(models.Model):
    content = models.TextField(max_length=1000)
    # createdBy = models.OneToOneField(
    #     User, on_delete=models.CASCADE, primary_key=True)
    # createdBy = models.OneToOneField(
    #     User, on_delete=models.PROTECT, primary_key=True)
    createdBy = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': True})
    date = models.DateField(default=date.today())

class Like(Post):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    likes = models.IntegerField()