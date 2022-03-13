from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page
from app1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("home/", cache_page(30)(views.home), name="home"),
]
