from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django import forms
from .forms import StudentForm
from .models import Student

class Thankyou(TemplateView):
    template_name = 'app1/ty.html'

class StundentCreateList(CreateView, ListView):
    model = Student
    form_class = StudentForm
    #fields = '__all__'
    #success_url = '/ty/'
    template_name = 'app1/student_form.html'

    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['name'].widget = forms.TextInput(attrs={'class': 'myclass'})
    #     return form


class StundentDetail(DetailView):
    model = Student

class StudentUpdate(UpdateView):
    model = Student
    success_url = '/ty/'
    fields = '__all__'

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class': 'myclass'})
        return form
    # form_class = None


    # template_name = None
    # template_engine = None
    # response_class = TemplateResponse
    # content_type = None

    # template_name_field = None
    # template_name_suffix = '_detail'

    

    # initial = {}
    
    
    # prefix = None

    # extra_context = None

    # queryset = None
    # slug_field = 'slug'
    # context_object_name = None
    # slug_url_kwarg = 'slug'
    # pk_url_kwarg = 'pk'
    # query_pk_and_slug = False


