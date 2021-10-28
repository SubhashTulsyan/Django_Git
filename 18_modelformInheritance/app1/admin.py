from django.contrib import admin
from .models import Registration
# Register your models here.
@admin.register(Registration)
class AdminReg(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'teacher_name', 'email', 'password']