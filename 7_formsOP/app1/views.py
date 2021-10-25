from django.shortcuts import render
from .forms import StudForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        stdform = StudForm(request.POST)
        print(stdform.is_valid())
        print(stdform.cleaned_data)
        if stdform.is_valid():
            #print('Name: ', request.POST['name']) Data may not be valid
            # and cleaned.
            print('Name: ', stdform.cleaned_data['name'])
            print('Email: ', stdform.cleaned_data['email'])
            print('Password: ', stdform.cleaned_data['pwd'])
    stdform = StudForm()
    return render(request, 'app1/index.html', {'sf': stdform})