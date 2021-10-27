from django.shortcuts import render
from .forms import StudentForm
from .models import Student
# Create your views here.
def home(request):
    if request.method == 'POST':
        sf = StudentForm(request.POST)
        if sf.is_valid():
            name = sf.cleaned_data['name']
            roll = sf.cleaned_data['roll']
            sm = Student(
                name = name,
                roll = roll
            )
            sm.save()
            sf = StudentForm()
            return render(request, 'app1/index.html', {'sf': sf})
        else:
            return render(request, 'app1/index.html', {'sf': sf})
    else:
        sf = StudentForm()
        return render(request, 'app1/index.html', {'sf': sf})

def data(request, num, ch):
    return render(request, 'app1/data.html', {'num': num, 'ch': ch})

def fetch(request):
    print('inside fetch')
    allStud = Student.objects.all()
    
    print(allStud[0])
    print(type(allStud[0]))
    return render(request, 'app1/data.html', {'allStud': allStud})

def fetch_id(request, id):
    stud = Student.objects.filter(id = id)[0]
    return render(request, 'app1/data.html', {'stud': stud})