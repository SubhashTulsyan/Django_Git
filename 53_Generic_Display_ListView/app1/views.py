from django.http import request
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student

# Create your views here.
class Home(ListView):
    model = Student
    # template_name = "app1/student.html"  # for custom template name
    # context_object_name = 'students' #for custom context name
    # template_name_suffix = '_get'
    # ordering = ['name']

    # def get_queryset(self):
    #     # return Student.objects.filter(name__iexact="ankit")
    #     return Student.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print("context: ", context)
    #     context["data"] = Student.objects.all().order_by("name")
    #     return context

    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'ankit':
    #         template_name = 'app1/ankit.html'
    #     # if self.request.user.is_superuser:
    #     #     template_name = 'app1/superuser.html'
    #     else:
    #         template_name = self.template_name

    #     return [template_name]

    # Eq to
    # student_list = Student.objects.all()
    # template_name = 'app1/student_list.html'
    # context = {'student_list': student_list}
