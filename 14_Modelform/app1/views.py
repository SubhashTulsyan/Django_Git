from django.shortcuts import render
from .forms import studentForm
from .models import student
# Create your views here.
def home(request):
    if request.method == 'POST':
        stu_1 = student.objects.get(pk = 1)
        sf_b = studentForm(request.POST, instance=stu_1)
        if sf_b.is_valid():
            print('Valid')
            sf_b.save()
            # print('Valid')
            # nm = sf_b.cleaned_data['name']
            # rl = sf_b.cleaned_data['roll']
            # em = sf_b.cleaned_data['email']
            # ps = sf_b.cleaned_data['password']
            # sm = student(
            #     name = nm,
            #     roll = rl,
            #     email = em,
            #     password = ps,
            # )
            # sm.save()
            sf_b = studentForm()
            return render(request, 'app1/index.html', {'sf': sf_b})
        else:
            print('Not Valid')
            return render(request, 'app1/index.html', {'sf': sf_b})

    else:
        sf = studentForm()
        return render(request, 'app1/index.html', {'sf': sf})
