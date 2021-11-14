from django.views.generic.detail import DetailView 
from django.views.generic.list import ListView 
from .models import Student
# Create your views here.
class Home(DetailView):
    model = Student
    # template_name = 'app1/student_detail.html'
    # context_object_name = 'student'
    # pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = self.model.objects.all()
        context["studentlist"] = students
        return context
    

class HomeList(ListView):
    model = Student
    
    