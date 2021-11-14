from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import Post
@receiver(post_delete, sender = Post)
def delUser(sender, instance, **kwargs):
    print('KWARGS: ', kwargs)
    print('instance: ', instance)
    instance.createdBy.delete()
