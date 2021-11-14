from django.views.generic.base import TemplateView, RedirectView



class MyRV(RedirectView):
    #url = 'https://google.com'
    #url = '/'
    pattern_name = 'myrva'
    permanent = True
    query_string = False

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context["name"])
    #     return context
    

    def get_redirect_url(self, *args, **kwargs):
        #print('-----1-----')
        #print('Args: ', args)
        kwargs['rk'] = 20
        print('kwargs: ', kwargs)
        return super().get_redirect_url(*args, **kwargs)