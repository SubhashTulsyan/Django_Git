from django.contrib import admin
from .models import Student, Teacher
# Register your models here.

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'roll', 'date']

@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'emp_id']
