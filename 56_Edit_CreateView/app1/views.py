from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django import forms
from .forms import StudentForm
from .models import Student


class Thankyou(TemplateView):
    template_name = "app1/ty.html"


class StundentDetail(DetailView):
    model = Student


class StudentView(CreateView):
    # success_url = '/ty/' # or define get_absolute_url in Model

    # Model
    # fields = '__all__'
    # model = Student
    def get_form(self):
        form = super().get_form()
        # form.fields['name'].widget = forms.TextInput(attrs={'class': 'myclass'})
        # form.fields['roll'].widget = forms.NumberInput(attrs={'class': 'myclass'})
        form.fields["doj"].widget = forms.DateInput(
            attrs={"class": "myclass", "type": "date"}
        )
        return form

    # Form
    form_class = StudentForm
    template_name = "app1/student_form.html"

    # template_name = None
    # template_engine = None
    # response_class = TemplateResponse
    # content_type = None

    # queryset = None
    # slug_field = 'slug'
    # context_object_name = None
    # slug_url_kwarg = 'slug'
    # pk_url_kwarg = 'pk'
    # query_pk_and_slug = False

    # initial = {}
    # form_class = None

    # prefix = None

    # extra_context = None
