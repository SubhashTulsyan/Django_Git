from datetime import date, datetime
from django.db.models import Q
from django.shortcuts import render
from .models import Student, Teacher
# Create your views here.
def home(request):
    #student = Student.objects.filter(roll__lte=12)
    
    #student = Student.objects.filter(roll__exact=12)
    # student = Student.objects.filter(roll__iexact=12)
    # student = Student.objects.filter(roll__gt=12)
    # student = Student.objects.filter(roll__gte=12)
    # student = Student.objects.filter(roll__lt=12)
    # student = Student.objects.filter(roll__lte=12)
    # student = Student.objects.filter(roll__startswith=12)
    # student = Student.objects.filter(roll__istartswith=12)
    # student = Student.objects.filter(roll__endswith=12)
    # student = Student.objects.filter(roll__iendswith=12)
    # student = Student.objects.filter(pass_date__range=('2020-01-01', '2021-01-01'))

    # student = Student.objects.filter(created_datetime__date=(2022,12,12))
    # student = Student.objects.filter(created_datetime__date__gt=(2022,12,12))

    # student = Student.objects.filter(created_datetime__year=2021)
    # student = Student.objects.filter(created_datetime__year__gt=2019)

    # student = Student.objects.filter(created_datetime__month=6)
    # student = Student.objects.filter(created_datetime__month__gt=5)

    # student = Student.objects.filter(created_datetime__day=6)
    # student = Student.objects.filter(created_datetime__day__gt=5)

    # same for week, week_day(day 1 sunday), quarter(start from Jan), 
    # time, hour, min, second, isnull, regex, iregex
    #student = Student.objects.filter(name__contains = 'BB')
    #student = Student.objects.filter(id__in = [1,2,4,6])
    



    print('students object: ', student, end='\n')
    print('sql qry: ', student.query)
    return render(request, 'app1/index.html', {'students': student})