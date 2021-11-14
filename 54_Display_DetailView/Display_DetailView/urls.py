from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('<int:id>/', views.Home.as_view(), name='home'),
    path('<int:pk>/', views.Home.as_view(), name='home'),
    path('', views.HomeList.as_view(), name='homeList'),
]
