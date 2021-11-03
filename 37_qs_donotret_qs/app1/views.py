from datetime import date, datetime
from django.db.models import Q
from django.shortcuts import render
from .models import Student, Teacher
# Create your views here.
def home(request):
    #student = Student.objects.get(pk = 2)

    #student = Student.objects.first()
    #student = Student.objects.order_by('-id').first()

    #student = Student.objects.last()
    #student = Student.objects.order_by('-id').last()

    #student = Student.objects.latest('pass_date')
    #student = Student.objects.earliest('pass_date')
    # student = Student.objects.all().exists()
    # print('bool: ', student)

    #s = Student.objects.create(name ='qwe', roll = 277, pass_date = '2021-01-01', created_datetime = datetime.now())
    # student, iscreated = Student.objects.get_or_create(name ='qwe', roll = 277, pass_date = '2021-01-01')
    # print('iscreated', iscreated)

    #student = Student.objects.filter(id = 9).update(name = 'ashaa')
    # student, created = Student.objects.update_or_create(id=12, defaults={'name': 'kohli',
    # 'roll': 12, 'pass_date': '2000-12-12'})
    # print('isCreated:', created)

    # list_students = [
    #     Student(name = 'a', roll = 1111, pass_date = '2000-12-12'),
    #     Student(name = 'a', roll = 1112, pass_date = '2000-12-12'),
    #     Student(name = 'a', roll = 1113, pass_date = '2000-12-12'),
    #     Student(name = 'a', roll = 1114, pass_date = '2000-12-12'),
    # ]
    # student = Student.objects.bulk_create(list_students)

    # students_data = Student.objects.all()
    # for stu in students_data:
    #     stu.name = 'bbbb'
    #     stu.pass_date = '1333-01-01'
    # student = Student.objects.bulk_update(students_data, ['name','pass_date'])

    #student = Student.objects.in_bulk() #all obj
    #student = Student.objects.in_bulk([]) #Empty dict
    # student = Student.objects.in_bulk([1,2])
    # for key,val in student.items():
    #     print(val.id)

    #student = Student.objects.filter(id=5).delete()

    student = Student.objects.all().count()

    #student = Student.objects.all().explain()

    #Book.objects.all().aggregate(Avg('price'))
        

    print('students object: ', student, end='\n')
    #print('sql qry: ', students.query)
    return render(request, 'app1/index.html', {'student': student})