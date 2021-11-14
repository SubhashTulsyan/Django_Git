from django.contrib import admin
from .models import Song
# Register your models here.
@admin.register(Song)
class SongModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'duration', 'sung_by']
