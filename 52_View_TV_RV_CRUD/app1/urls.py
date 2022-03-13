from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.AddShow.as_view(), name="addShow"),
    path("delete/<int:id>/", views.Delete.as_view(), name="delete"),
    path("update/<int:id>/", views.Update.as_view(), name="update"),
]
