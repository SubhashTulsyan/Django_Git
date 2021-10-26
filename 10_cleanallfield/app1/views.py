from django.shortcuts import render
from .forms import studForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        sf = studForm(request.POST)
        if sf.is_valid():
            print(sf.cleaned_data['name'])
            print(sf.cleaned_data['email'])
            return render(request, 'app1/index.html', {'sf': sf})
        else:
            print('Form is not valid.')
            return render(request, 'app1/index.html', {'sf': sf})

    else:
        sf = studForm()
        return render(request, 'app1/index.html', {'sf': sf})