from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import StudentForm, TeacherForm
# Create your views here.
def home(request):
    sf = StudentForm()
    tf = TeacherForm()
    data = {
        'sf': sf,
        'tf': tf,
    }
    return render(request, 'app1/index.html', data)