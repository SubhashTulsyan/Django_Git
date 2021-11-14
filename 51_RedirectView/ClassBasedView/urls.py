"""ClassBasedView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name = 'app1/index.html'), name='home'),
    path('index/', views.RedirectView.as_view(url = '/'), name='index'),
    path('google/', views.RedirectView.as_view(url = 'https://google.com'), name='google'),
    path('pat/', views.RedirectView.as_view(pattern_name = 'index'), name='pat'),
    path('myrv/', views.MyRV.as_view(), name='myrv'),
    # path('myrv/<slug:rk>/', views.MyRV.as_view(), name='myrv'),
    # path('<slug:rk>/', views.TemplateView.as_view(template_name = 'app1/index.html'), name='myrva'),
    path('myrv/<int:rk>/', views.MyRV.as_view(), name='myrv'),
    path('<int:rk>/', views.TemplateView.as_view(template_name = 'app1/index.html'), name='myrva'),
    
    ]
