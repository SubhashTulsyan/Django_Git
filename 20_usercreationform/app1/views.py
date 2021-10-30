from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm,\
AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,\
update_session_auth_hash
from django.contrib.auth.models import User
from .forms import SignUpForm, ProfileForm, ProfileAdminForm


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
        af = AuthenticationForm(request = request, data = request.POST)
        if af.is_valid():
            uname = af.cleaned_data['username']
            print(uname)
            upass = af.cleaned_data['password']
            print(upass)
            user = authenticate(username = uname, password = upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return HttpResponseRedirect('/profile/')
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/profile/')
        else:
            af = AuthenticationForm()
    return render(request, 'app1/login.html', {'af': af})

def profile(request):
    if request.user.is_authenticated:
        name = request.user
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
        return render(request, 'app1/profile.html' , {'name': name, 'ucf': ucf,
        'users': users})
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
