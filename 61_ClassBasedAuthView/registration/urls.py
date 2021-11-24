from django.contrib.auth import decorators
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from . import views

#import django.contrib.auth.urls
urlpatterns = [
    # path('profile/', login_required(views.ProfileTV.as_view()), name='profile'),
    # path('about/', staff_member_required(views.AboutTV.as_view()), name='about'),
    path('profile/', views.ProfileTV.as_view(), name='profile'),
    path('about/', views.AboutTV.as_view(), name='about'),
]
