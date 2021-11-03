from django.db.models import Q
from django.shortcuts import render
from .models import Student, Teacher
# Create your views here.
def home(request):
    #students = Student.objects.all()

    #students = Student.objects.filter(roll = 2)

    #students = Student.objects.exclude(roll = 2)

    #students = Student.objects.order_by('name')
    #students = Student.objects.order_by('?')
    #students = Student.objects.order_by('-roll', 'id')

    #students = Student.objects.order_by('id').reverse()[:2]

    #students = Student.objects.values()
    #students = Student.objects.values('name', 'roll')

    #students = Student.objects.distinct('name')

    #students = Student.objects.values_list(named=True)
    #students = Student.objects.values_list('name', 'roll', named=True)
    #students = Student.objects.values_list('name', flat=True)
    
    #students = Student.objects.using('default')

    #students = Student.objects.dates('pass_date', kind='year', order='ASC')
    #students = Student.objects.dates('pass_date', kind='month', order='ASC')
    #students = Student.objects.dates('pass_date', kind='week', order='ASC')
    #students = Student.objects.dates('pass_date', kind='day', order='ASC')

    #students = Student.objects.datetimes('created_datetime', kind='year', order='ASC', tzinfo=None)
    # students = Student.objects.datetimes('pass_date', kind='month', order='ASC', tzinfo=None)
    # students = Student.objects.datetimes('pass_date', kind='week', order='ASC', tzinfo=None)
    # students = Student.objects.datetimes('pass_date', kind='day', order='ASC', tzinfo=None)

    # students = Student.objects.none()

    #qs1 = Student.objects.values_list('name', 'roll')
    #qs2 = Student.objects.values_list('name', 'roll')
    #students = qs1.union(qs2, all=True)
    #students = qs1.intersection(qs2)
    #students = qs1.difference(qs2)

    # rawQuery = 'select * from app1_student limit 5'
    # students = Student.objects.raw(rawQuery)

    qs1 = Student.objects.filter(roll = 1)
    qs2 = Student.objects.filter(id = 2)
    #students = qs1 & qs2
    #students = Student.objects.filter(roll = 1, id = 1)
    #students = Student.objects.filter(Q(roll = 1) & Q(id = 1))


    #students = qs1 | qs2
    #students = Student.objects.filter(Q(roll = 1) | Q(id = 1))



    

    print('students qryset: ', students, end='\n')
    print('sql qry: ', students.query)
    return render(request, 'app1/index.html', {'students': students})