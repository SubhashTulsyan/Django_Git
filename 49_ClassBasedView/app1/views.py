from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .forms import StudentForm
# Create your views here.
class homeView(View):
    name = 'View'
    def get(self, request):
        return HttpResponse(f'My Home : {self.name}')
class ChildHomeView(homeView):
    def get(self, request):
        return HttpResponse(f'My Home : {self.name}')

##########################################
class TemplateEx(View):
    def get(self, request):
        return render(request, 'app1/index.html')

class FormTestclass(View):
    template_name = ''
    def get(self, request):
        sf = StudentForm()
        data = {'sf': sf}
        return render(request, self.template_name, context=data)
    def post(self, request):
        sf = StudentForm(request.POST)
        if sf.is_valid():
            msg = sf.cleaned_data['name']
        else:
            msg = 'NOT Ok'
        return render(request, self.template_name, context={'msg': msg})

def formtest(request, template_name):
    return render(request, template_name)













class FormTestTemp(View):
    def get(self, request):
        sf = StudentForm()
        data = {'sf': sf}
        return render(request, self.template_name, context=data)
    def post(self, request):
        sf = StudentForm(request.POST)
        if sf.is_valid():
            msg = sf.cleaned_data['name']
        else:
            msg = 'NOT Ok'
        return render(request, self.template_name, context={'msg': msg})