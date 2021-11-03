from django.contrib import admin
from .models import MarketModel, ProxyMarketModel
# Register your models here.
@admin.register(MarketModel)
class MarketModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
@admin.register(ProxyMarketModel)
class ProxyMarketModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
