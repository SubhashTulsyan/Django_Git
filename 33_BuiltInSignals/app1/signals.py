from django.contrib.auth.signals import user_logged_in, user_logged_out,\
    user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete,\
    post_delete, pre_init, post_init, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

#Login
@receiver(user_logged_in, sender = User)
def login_suc(sender, request, user, **kwargs):
    print('------------login suc--------')
    print('Sender:', sender)
    print('Request:', request)
    print('User:', user)
    print('User Password:', user.password)
    print(f'User kwargs: {kwargs}')

#user_logged_in.connect(login_suc, sender=User)

#logout
@receiver(user_logged_out, sender = User)
def logout_suc(sender, user, request, **kwargs):
    print('------------logout suc--------')
    print('Sender:', sender)
    print('Request:', request)
    print('User:', user)
    print('User Password:', user.password)
    print(f'kwargs: {kwargs}')

#user_logged_out.connect(logout_suc, sender=User)

#login Failed
@receiver(user_login_failed)
def login_fail(sender, credentials, request, **kwargs):
    print('------------login fail--------')
    print('Sender:', sender)
    print('Request:', request)
    print('credentials:', credentials)
    print(f'kwargs: {kwargs}')

#user_login_failed.connect(login_fail)

#Pre Save
@receiver(pre_save, sender = User)
def pre_sve(sender, instance, raw, using, update_fields, **kwargs):
    print('------------Pre Save--------')
    print('Sender:', sender)
    print('instance:', instance)
    print('raw:', raw)
    print('using:', using)
    print('update_fields:', update_fields)
    print(f'kwargs: {kwargs}')

#Post Save
@receiver(post_save, sender = User)
def post_save(sender, instance, created, update_fields, raw, using, **kwargs):
    if created:
        print('------------Post Save Created--------')
        print('Sender:', sender)
        print('instance:', instance)
        print('created:', created)
        print('update_fields:', update_fields)
        print('raw:', raw)
        print('using:', using)
        print(f'kwargs: {kwargs}')
    else:
        print('------------Post Save Updated--------')
        print('Sender:', sender)
        print('instance:', instance)
        print('created:', created)
        print('update_fields:', update_fields)
        print('raw:', raw)
        print('using:', using)
        print(f'kwargs: {kwargs}')

#Pre Delete
@receiver(pre_delete, sender = User)
def pre_del(sender, instance, using, **kwargs):
    print('------------Pre Delete--------')
    print('Using: ', using)
    print('instance:', instance)
    print(f'kwargs: {kwargs}')
#Post Delete
@receiver(post_delete, sender = User)
def post_del(sender, instance, using, **kwargs):
    print('------------Post Delete--------')
    print('Using: ', using)
    print('instance:', instance)
    print(f'kwargs: {kwargs}')
#Pre Init
@receiver(pre_init, sender = User)
def pre_ini(sender, *args, **kwargs):
    print('------------Pre Init--------')
    # print('Using: ', using)
    # print('instance:', instance)
    print(f'Args: {args}')
    print(f'kwargs: {kwargs}')
#Post Init
@receiver(post_init, sender = User)
def post_ini(sender, *args, **kwargs):
    print('------------Post init--------')
    # print('Using: ', using)
    # print('instance:', instance)
    print(f'Args: {args}')
    print(f'kwargs: {kwargs}')
#Request Started
@receiver(request_started)
def req_started(sender, *args, **kwargs):
    print('------------request_started--------')
    # print('Using: ', using)
    # print('instance:', instance)
    print(f'Args: {args}')
    print(f'kwargs: {kwargs}')
#Req Finished
@receiver(request_finished)
def req_finish(sender, *args, **kwargs):
    print('------------request_finished--------')
    # print('Using: ', using)
    # print('instance:', instance)
    print(f'Args: {args}')
    print(f'kwargs: {kwargs}')
#got_request_exception
@receiver(got_request_exception)
def req_exception(sender, request, *args, **kwargs):
    print('------------got_request_exception--------')
    # print('Using: ', using)
    # print('instance:', instance)
    print(f'Args: {args}')
    print(f'kwargs: {kwargs}')
#Pre_migrate
@receiver(pre_migrate)
def pre_mig(sender, app_config, verbosity, interactive, using, apps, **kwargs):
    print('------------pre_migrate--------')
    # print('Using: ', using)
    # print('instance:', instance)
    print('sender: ', sender)
    print(f'kwargs: {kwargs}')
#Post_migrate
@receiver(post_migrate)
def post_mig(sender, app_config, verbosity, interactive, using, apps, **kwargs):
    print('------------post_migrate--------')
    # print('Using: ', using)
    # print('instance:', instance)
    print('sender: ', sender)
    print(f'kwargs: {kwargs}')

# DB Connection Created
@receiver(connection_created)
def connection_create(sender, *args, **kwargs):
    print('--connection_create--')
    print('args: ', args)
    print('kwargs: ', kwargs)