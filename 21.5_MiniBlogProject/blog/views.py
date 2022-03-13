from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import Group, Permission
from .models import Post
from .forms import AddPost, LoginForm, SignUpForm
# Create your views here.
def home(request):
    posts = Post.objects.all()
    data = {
        'posts': posts
    }
    return render(request, 'blog/home.html', data)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        fullName = user.get_full_name()
        print(fullName)
        groups = user.groups.all()
        print(groups)
        data = {
            'posts': posts,
            'fullName': fullName,
            'groups': groups,
        }
        return render(request, 'blog/dashboard.html', data)
    else:
        return HttpResponseRedirect('/login/')
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def signup(request):
    # data = {}
    # print(type(data))
    if request.method == 'POST':
        suf = SignUpForm(request.POST)
        print('in post')
        if suf.is_valid():
            print('is valid')
            user = suf.save()
            grp = Group.objects.get(name = 'Author')
            user.groups.add(grp)
            messages.success(request, 'Author Registered Successfully !!')
            #suf = SignUpForm()
            # message = 'User Registered Successfully !!'
            # data['message'] = message
            # data['suf'] = suf
        # else:
        #     suf = SignUpForm()
        #     data['suf'] = suf
    else:
        suf = SignUpForm()
        # data['suf'] = suf
    data = {
        'suf': suf,
    }
    return render(request, 'blog/signup.html', data)

def user_login(request):
    print('login')
    if not request.user.is_authenticated:
        print('NA')
        if request.method == 'POST':
            lf = LoginForm(request = request, data = request.POST)
            print('post', lf.is_valid())
            if lf.is_valid():
                uname = lf.cleaned_data['username']
                upass = lf.cleaned_data['password']
                user = authenticate(request, username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'User Logged-in successfully !!', extra_tags='ok_Login')
                    return HttpResponseRedirect('/dashboard/')
        else:
            lf = LoginForm()
        data = {'lf': lf}
        return render(request, 'blog/login.html', data)
    else:
        return HttpResponseRedirect('/dashboard/')

def add(request):
    if request.method == 'POST':
        ap = AddPost(request.POST, request.FILES)
        if ap.is_valid():
            ap.save()
            return HttpResponseRedirect('/dashboard/')
    ap = AddPost()
    data = {
        "ap": ap,
    }
    return render(request, 'blog/addPost.html', data)
def edit(request, pk):
    rec = Post.objects.get(id=pk)
    if request.method == 'POST':
        ap = AddPost(request.POST, request.FILES, instance=rec)
        if ap.is_valid():
            ap.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        postForm = AddPost(instance=rec)
        data = {
            'ap': postForm,
        }
        return render(request, 'blog/addPost.html', data)

def delete(request, pk):
    if request.user.is_authenticated and request.method == 'POST':
        rec = Post.objects.get(pk = pk)
        if rec is not None:
            rec.delete()
            return HttpResponseRedirect('/dashboard/')
