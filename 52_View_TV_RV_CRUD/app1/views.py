from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views.generic.base import View, TemplateView, RedirectView
from .forms import UserForm
from .models import User

# Create your views here.
class Delete(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        #print('Args: ', args)
        print('Kwargs: ', kwargs)
        user = User(id = kwargs['id'])
        user.delete()
        return super().get_redirect_url(*args, **kwargs)

class AddShow(TemplateView):
    template_name = 'app1/addshow.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uf = UserForm()
        users = User.objects.all()
        context['uf'] = uf
        context['users'] = users
        return context

    def post(self, request):
        uf = UserForm(request.POST)
        if uf.is_valid():
            nm = uf.cleaned_data['name']
            rl = uf.cleaned_data['roll']
            # pwd = uf.cleaned_data['password']
            user = User(
                name = nm,
                roll = rl,
                #password = pwd
            )
            user.save()
            return HttpResponseRedirect('/')

class Update(TemplateView, RedirectView):
    template_name = 'app1/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('context: ', context)
        user = User.objects.get(id= context['id'])
        uf = UserForm(instance=user)
        context['uf'] = uf
        context['user_id'] = context['id']
        return context

    def post(self, request, *args, **kwargs):
        print('args: ', args)
        print('kwargs: ', kwargs)
        user = User.objects.get(pk=kwargs['id'])
        uf = UserForm(request.POST, instance=user)
        if uf.is_valid():
            uf.save()
        return HttpResponseRedirect('/')