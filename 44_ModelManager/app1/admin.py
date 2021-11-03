from django.contrib import admin
from .models import Student, StudentProxy
# Register your models here.
@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    
@admin.register(StudentProxy)
class StudentProxyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')