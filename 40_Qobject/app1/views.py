from datetime import date, datetime
from django.db.models import Q, Avg, Sum, Min, Max, Count, StdDev, Variance
from django.shortcuts import render
from .models import Student, Teacher
# Create your views here.
def home(request):
    # student = Student.objects.filter(
    #     Q(pass_date = '1333-01-01')
    #     &
    #     Q(roll = 2),
    #     )
    #student = Student.objects.filter(~Q(pass_date = '1333-01-01'))

    student = Student.objects.filter(
        Q(pass_date = '1333-01-01'))[:5]

    print('students object: ', student, end='\n')
    #print('sql qry: ', student.query)
    return render(request, 'app1/index.html', {'students': student})