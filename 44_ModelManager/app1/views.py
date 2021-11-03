from django.shortcuts import render
from .models import Student, StudentProxy
# Create your views here.
def home(request):
    #students = Student.objects.all()
    #students = Student.students.notEqualManager(id = 2)
    students = StudentProxy.students.notEqualManager(id = 2)
    return render(request, 'app1/index.html', {'students': students})