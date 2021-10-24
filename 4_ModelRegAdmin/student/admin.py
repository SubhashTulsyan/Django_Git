from typing import OrderedDict
from django.contrib import admin
from .models import Student

# Approach 1
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'branch',)
# admin.site.register(Student, StudentAdmin)

# Approach 2
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','roll', 'name', 'branch',)
