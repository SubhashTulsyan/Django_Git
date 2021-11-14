from django.views.generic.base import TemplateView



class Home(TemplateView):
    template_name = 'app1/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Subhash'
        print('kwargs: ', kwargs)
        #context = {'name': 'Subhash'} #here extra_context data will not populate
        return context