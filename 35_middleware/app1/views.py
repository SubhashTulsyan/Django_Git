from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def home(request):
    print('inside home view')
    return HttpResponse('Home View Called')

def excp(request):
    a = 5/0
    return HttpResponse('excp')

def template_process(request):
    context = {
        'name': 'Subh',
    }
    return TemplateResponse(request, 'app1/temp.html', context=context)