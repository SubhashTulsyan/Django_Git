import django
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm,\
AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,\
update_session_auth_hash
from django.contrib.auth.models import User
from django.utils import version
from .forms import SignUpForm, ProfileForm, ProfileAdminForm
from django.core.cache import cache


# Create your views here.
def signup_1(request):

    if request.method == 'POST':
        ucf = UserCreationForm(request.POST)
        if ucf.is_valid():
            ucf.save()
            ucf = UserCreationForm()
    else: 
        ucf = UserCreationForm()
    return render(request, 'app1/signup.html', {'ucf': ucf})

def signup_2(request):

    if request.method == 'POST':
        ucf = SignUpForm(request.POST)
        if ucf.is_valid():
            ucf.save()
            messages.success(request, 'User Created successfully.')
            ucf = SignUpForm()
    else: 
        ucf = SignUpForm()
    return render(request, 'app1/signup.html', {'ucf': ucf})

def login_user(request):
    if request.method == 'POST':
        print('inpost')
        af = AuthenticationForm(request = request, data = request.POST)
        print('user_name req: ', request.POST['username'])
        print('isvalid flag: ', af.is_valid())
        if af.is_valid():
            print('isvalid')
            uname = af.cleaned_data['username']
            print('uname', uname)
            upass = af.cleaned_data['password']
            print('upass', upass)
            user = authenticate(username = uname, password = upass)
            print('user authenticate: ', user)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return HttpResponseRedirect('/profile/')
        else:
            count = cache.get('logfail', version = request.POST['username'])
            print('count in view', count)
            if count >=3:
                lock_msg = 'Your account is locked for 1 min'
                return render(request, 'app1/login.html', {'af': af, 'lock_msg': lock_msg})
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/profile/')
        else:
            af = AuthenticationForm()
    return render(request, 'app1/login.html', {'af': af})

def profile(request):
    if request.user.is_authenticated:
        name = request.user
        ip = request.session.get('ip', 0)
        ct = cache.get('count', version = name.pk)
        if request.method == 'POST':
            if request.user.is_superuser:
                ucf = ProfileAdminForm(instance = request.user, data = request.POST)
                users = User.objects.all()
            else:
                ucf = ProfileForm(instance = request.user, data = request.POST)
                users = None
            if ucf.is_valid():
                ucf.save()
                messages.success(request, 'Updated successfully')
        else:
            if request.user.is_superuser:
                ucf = ProfileAdminForm(instance = request.user)
                users = User.objects.all()
                #print(users)
            else:
                ucf = ProfileForm(instance = request.user)
                users = None
                #ip = request.session.get('ip', 0)
                #ct = cache.get('count', version = request.user.pk)
        return render(request, 'app1/profile.html' , {'name': name, 'ucf': ucf,
        'users': users, 'ip': ip, 'ct': ct})
    else:
        return HttpResponseRedirect('/login/')

def userdetails(request , id):
    if request.user.is_authenticated:
        user = User.objects.get(pk = id)
        fm = ProfileAdminForm(instance = user)
        return render(request, 'app1/userdetails.html', {'fm': fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def passchange(request):
    if request.method == 'POST':
        ps = PasswordChangeForm(user = request.user, data = request.POST)
        if ps.is_valid():
            ps.save()
            update_session_auth_hash(request, ps.user)
            return HttpResponseRedirect('/profile/')
    elif request.user.is_authenticated:
        ps =PasswordChangeForm(user = request.user)
        return render(request, 'app1/passchange.html', {'ps': ps})
    else:
        return HttpResponseRedirect('/login/')
    

def forgotpass(request):
    if request.method == 'POST':
        ps = SetPasswordForm(user = request.user, data = request.POST)
        if ps.is_valid():
            ps.save()
            update_session_auth_hash(request, ps.user)
            return HttpResponseRedirect('/profile/')
    elif request.user.is_authenticated:
        ps =SetPasswordForm(user = request.user)
        return render(request, 'app1/forgotpass.html', {'ps': ps})
    else:
        return HttpResponseRedirect('/login/')
