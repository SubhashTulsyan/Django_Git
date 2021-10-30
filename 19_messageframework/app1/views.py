from django.shortcuts import render
from django.contrib import messages
from .forms import StudentForm
# Create your views here.

# Message Framework in Django.

#DEBUG 10
#INFO 20
#SUCCESS 25
#WARNING 30
#ERROR 40

def home(request):
    if request.method == 'POST':
        sf = StudentForm(request.POST)
        if sf.is_valid():
            sf.save()
            for mes in messages.get_messages(request):
                print(mes)
            messages.set_level(request, messages.DEBUG)
            print(messages.get_level(request))
            #add_message(request, message='Test success', level=messages.SUCCESS)
            #messages.success(request, message='Test success')
            messages.debug(request, message='Debug success')
            messages.info(request, message='Info success')
            messages.success(request, message='success success')
            messages.warning(request, message='warn success')
            messages.error(request, message='Error success')
            
            for mesa in messages.get_messages(request):
               print(mesa)
            sf = StudentForm()
        return render(request, 'app1/index.html', {'sf': sf})
    else:
        sf = StudentForm()
        return render(request, 'app1/index.html', {'sf': sf})


    # messages.debug(request, message='Test Debug', extra_tags='ET_Debug')
    # messages.info(request, message='Test info', extra_tags='ET_Info')
    # messages.success(request, message='Test success', extra_tags='ET_success')
    # messages.warning(request, message='Test warning', extra_tags='ET_warning')
    # messages.error(request, message='Test error', extra_tags='ET_error')
    return render(request, 'app1/index.html')