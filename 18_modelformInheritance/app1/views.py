from django.shortcuts import render
from .forms import StudentForm, TeacherForm
# Create your views here.

def st(request):
    if request.method == 'POST':
        sf = StudentForm(request.POST)
        if sf.is_valid():
            sf.save()
            sf = StudentForm()
            return render(request, 'app1/index.html', {'sf': sf})
        else:
            return render(request, 'app1/index.html', {'sf': sf})
    else:
        sf = StudentForm()
        return render(request, 'app1/index.html', {'sf': sf})

def te(request):
    if request.method == 'POST':
        tf = TeacherForm(request.POST)
        if tf.is_valid():
            tf.save()
            tf = TeacherForm()
            return render(request, 'app1/index.html', {'tf': tf})
        else:
            return render(request, 'app1/index.html', {'tf': tf})
    else:
        tf = TeacherForm()
        return render(request, 'app1/index.html', {'tf': tf})

    
