from django.shortcuts import render
from .forms import studforms
# Create your views here.
def home(request):
    fw = studforms()
    return render(request, 'app1/index.html', {'fw': fw})