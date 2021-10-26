from django.shortcuts import render
from .forms import signUpForm
from .models import student
# Create your views here.
def home(request):
    if request.method == 'POST':
        sf = signUpForm(request.POST)
        if sf.is_valid():
            nm = sf.cleaned_data['name']
            em = sf.cleaned_data['email']
            #sm = student(name = nm, email = em)
            # sm = student(id = 1, name = nm, email = em)
            # sm.save()
            sm = student(id = 2)
            sm.delete()
            sf = signUpForm()
            return render(request, 'app1/index.html', {'sf': sf})
        else:
            return render(request, 'app1/index.html', {'sf': sf})
    else:
        sf = signUpForm()
        return render(request, 'app1/index.html', {'sf': sf})