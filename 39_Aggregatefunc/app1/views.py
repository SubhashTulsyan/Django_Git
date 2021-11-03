from datetime import date, datetime
from django.db.models import Q, Avg, Sum, Min, Max, Count, StdDev, Variance
from django.shortcuts import render
from .models import Student, Teacher
# Create your views here.
def home(request):
    student = Student.objects.all().aggregate(
        Avg('roll'),
        Min('id'),
        Max('roll'),
        Count('id'),
        Sum('id'),
        StdDev('id'),
        Variance('id'),
        )
    print('students object: ', student, end='\n')
    #print('sql qry: ', student.query)
    return render(request, 'app1/index.html', {'students': student})