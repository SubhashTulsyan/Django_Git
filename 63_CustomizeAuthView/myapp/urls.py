from django.contrib.auth import forms, views as auth_views
from django.urls import path
from django.views.generic.base import TemplateView
from .forms import LoginForm
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="myapp/home.html"), name="home"),
    # path('login/', auth_views.LoginView.as_view(
    #     template_name='myapp/login.html',
    #     authentication_form = LoginForm,
    #     ), name='login'),
    path("login/", views.MyLoginView.as_view(), name="login"),
    path(
        "dashboard/",
        TemplateView.as_view(template_name="myapp/dashboard.html"),
        name="dashboard",
    ),
    path(
        "profile/",
        TemplateView.as_view(template_name="myapp/profile.html"),
        name="profile",
    ),
    # path('logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),
    path("logout/", views.MyLogoutView.as_view(), name="logout"),
    # path('changepass/', auth_views.PasswordChangeView.as_view(
    #     template_name='myapp/changepass.html',
    #     success_url = '/myapp/changepassdone/'
    #     ), name='changepass'),
    path("changepass/", views.MyPasswordChangeView.as_view(), name="changepass"),
    # path('changepassdone/', auth_views.PasswordChangeDoneView.as_view(template_name='myapp/changepassdone.html'), name='changepassdone'),
    path(
        "changepassdone/",
        views.MyPasswordChangeDoneView.as_view(),
        name="changepassdone",
    ),
]
