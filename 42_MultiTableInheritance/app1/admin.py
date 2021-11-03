from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(FatherModel)
class FatherModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'father_name')
    
@admin.register(SonModel)
class SonModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'son_name', 'father_name')

@admin.register(DaughterModel)
class DaughterModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'daughter_name', 'father_name')
