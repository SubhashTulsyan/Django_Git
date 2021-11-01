from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.cache import cache
@receiver(user_logged_in, sender = User)
def loggedin(sender, request, user, *args, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ip

    count = cache.get('count', 0, version = user.pk)
    newcount = count + 1
    cache.set('count', newcount, 60*60*24, version = user.pk)
    #print(user.pk)


@receiver(user_login_failed)
def user_loginFailed(sender, request, credentials, *args, **kwargs):
    print('--------Login failed---------')
    count = cache.get('logfail', 0, version = credentials['username'])
    newcount = count + 1
    print('newcount', newcount)
    print('request.user', request.user)
    print('Credential username', credentials['username'])
    print(*args)
    print(f'afaf: {kwargs}')
    cache.set('logfail', newcount, 60, version = credentials['username'])

