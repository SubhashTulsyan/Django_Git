from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.StudentView.as_view(), name="home"),
    path("ty/", views.Thankyou.as_view(), name="ty"),
    path("detail/<int:pk>", views.StundentDetail.as_view(), name="detail"),
]
