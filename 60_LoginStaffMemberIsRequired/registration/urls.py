from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.urls
from . import views
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
]
