from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import StudentForm


class Thankyou(TemplateView):
    template_name = "app1/ty.html"


class StudentView(FormView):
    initial = {
        "name": "Initial Name",
        "roll": "-1",
        "doj": "2009-01-01",
    }
    form_class = StudentForm
    success_url = "/ty/"
    # prefix = None
    template_name = "app1/index.html"
    # template_engine = None
    # response_class = TemplateResponse
    # content_type = None

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)
