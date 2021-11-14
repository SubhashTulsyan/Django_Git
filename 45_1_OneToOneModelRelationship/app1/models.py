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
        User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': False})
    date = models.DateField(default=date.today())

class Like(Post):
    postId = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='post_id')
    likes = models.IntegerField()