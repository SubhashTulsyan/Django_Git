from django.contrib import admin
from .models import Page, Post, Song
# Register your models here.
@admin.register(Page)
class PageModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'publishDate', 'user']
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'publishDate', 'user']
@admin.register(Song)
class SongModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'duration', 'sung_by']