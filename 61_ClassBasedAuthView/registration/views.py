from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
decorators = [login_required, staff_member_required]
@method_decorator(decorators, name='dispatch')
class ProfileTV(TemplateView):
    template_name = 'registration/profile.html'

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

@method_decorator(staff_member_required, name='dispatch')
class AboutTV(TemplateView):
    template_name = 'registration/about.html'

    # @method_decorator(staff_member_required)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

