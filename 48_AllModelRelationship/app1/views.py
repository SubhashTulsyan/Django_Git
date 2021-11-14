from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Page, Post, Song
# Create your views here.
def all_data(request):
    pagedata = Page.objects.all()
    postdata = Post.objects.all()
    songdata = Song.objects.all()
    t = User.objects.filter(singer_id__singer=2)
    alldata = {
        'pagedata': pagedata,
        'postdata': postdata,
        'songdata': songdata,
        't': t,
    }
    return render(request, 'app1/alldata.html', context=alldata)
