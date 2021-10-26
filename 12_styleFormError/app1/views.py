from django.shortcuts import render
from .forms import signUpForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        sf = signUpForm(request.POST)
        if sf.is_valid():
            print(sf.cleaned_data['name'])
            print(sf.cleaned_data['email'])
            print(sf.cleaned_data['pwd'])
            print(sf.cleaned_data['pwd_cfm'])
            sf = signUpForm()
            return render(request, 'app1/index.html', {'sf': sf})
        else:
            return render(request, 'app1/index.html', {'sf': sf})
    else:
        sf = signUpForm()
        return render(request, 'app1/index.html', {'sf': sf})