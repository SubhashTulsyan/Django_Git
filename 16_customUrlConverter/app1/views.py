from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request, year):
    return HttpResponse(f'abc: {year}')