from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('id')
    paginator = Paginator(posts, per_page=3, orphans=1)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)
    return render(request, 'blog/home.html', {'page_obj': page_obj})