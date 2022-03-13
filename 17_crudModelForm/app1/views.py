from django.shortcuts import redirect, render
from .forms import UserForm
from .models import UserModel
# Create your views here.
def update(request, id):
    if request.method == 'POST':
        print(id)
        print('a')
        user = UserModel.objects.get(pk=id)
        uf = UserForm(request.POST, instance=user)
        if uf.is_valid():
            uf.save()
        return redirect('/')

    else:
        user = UserModel.objects.get(id= id)
        uf = UserForm(instance=user)
        return render(request, 'app1/update.html', {'uf': uf, 'user_id': id})
        
def delete(request, id):
    user = UserModel(id = id)
    #user = User.objects.get(pk = id)
    user.delete()
    return redirect('/')


def addShow(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # nm = uf.cleaned_data['name']
            # rl = uf.cleaned_data['roll']
            # pwd = uf.cleaned_data['password']
            # user = User(
            #     name = nm,
            #     roll = rl,
            #     password = pwd
            # )
            uf.save()
            uf = UserForm()
            users = UserModel.objects.all()
            return render(request, 'app1/addshow.html', {'uf': uf, 'users': users})
        else:
            return render(request, 'app1/addshow.html', {'uf': uf})
    else:
        uf = UserForm()
        users = UserModel.objects.all()
        return render(request, 'app1/addshow.html', {'uf': uf, 'users': users})