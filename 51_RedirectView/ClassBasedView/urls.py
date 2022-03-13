from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.TemplateView.as_view(template_name="app1/index.html"), name="home"),
    path("index/", views.RedirectView.as_view(url="/"), name="index"),
    path(
        "google/", views.RedirectView.as_view(url="https://google.com"), name="google"
    ),
    path("pat/", views.RedirectView.as_view(pattern_name="index"), name="pat"),
    path("myrv/", views.MyRV.as_view(), name="myrv"),
    # path('myrv/<slug:rk>/', views.MyRV.as_view(), name='myrv'),
    # path('<slug:rk>/', views.TemplateView.as_view(template_name = 'app1/index.html'), name='myrva'),
    path("myrv/<int:rk>/", views.MyRV.as_view(), name="myrv"),
    path(
        "<int:rk>/",
        views.TemplateView.as_view(template_name="app1/index.html"),
        name="myrva",
    ),
]
