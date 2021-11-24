from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.http import Http404
class PostList(ListView):
    template_name = 'blog/home.html'
    model = Post
    ordering = ['id']
    #paginate_by = 3 #page_obj by default in context
    paginate_orphans = 1
    page_size = None

    # def get_context_data(self, **kwargs):
    #     try:
    #         print('try kwargs: ', self.kwargs)
    #         return super(PostList, self).get_context_data(**kwargs)
    #     except Http404:
    #         self.kwargs['page'] = 1
    #         print('except kwargs: ', self.kwargs)
    #         return super(PostList, self).get_context_data(**kwargs)

    def paginate_queryset(self, queryset, page_size):
        try:
            print('try page_size: ')
            return super(PostList, self).paginate_queryset(queryset, page_size)
        except Http404:
            self.kwargs['page'] = 1
            print('try page_size: ', self.page_size)
            return super(PostList, self).paginate_queryset(queryset, page_size)

class PostData(DetailView):
    template_name = 'blog/details.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('context: ', context)
        return context
    
    