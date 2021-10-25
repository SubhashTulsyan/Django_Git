from enum import auto
from django.http.request import HttpRequest
from django.shortcuts import render
from .forms import studentform
# Create your views here.
def home(request):
    ini = {
        'roll': 53,
        'branch': '-1',
    }

    sf = studentform(auto_id='aa_%s', label_suffix=': ', initial=ini)
    sf.order_fields(field_order=['roll', 'name', 'branch'])
    return render(request, 'app1/index.html', {'sf': sf})