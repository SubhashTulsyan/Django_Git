from django.contrib import admin
from django.urls import path
from registration import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('login/', views.LoginView.as_view(template_name = 'registration/login.html'), name='mylogin'),
    path("login/", views.MyLoginView.as_view(), name="mylogin"),
    path("logout/", views.LogoutView.as_view(), name="mylogout"),
    # path('logout/', views.MyLogoutView.as_view(), name='mylogout'),
]
