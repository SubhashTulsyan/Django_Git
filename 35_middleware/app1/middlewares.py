from django.shortcuts import HttpResponse


def custom_middleware(get_response):
    print('custom_middleware initialized')

    def custom_middlewareinsidefn(request):
        print('Before View: custom_middlewareinsidefn')
        response = get_response(request)
        print('After View: custom_middlewareinsidefn')
        return response
    return custom_middlewareinsidefn

class classbasedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('classbasedMiddleware initialized')

    def __call__(self, request):
        print('Before View: classbasedMiddleware')
        response = self.get_response(request)
        print('After View: classbasedMiddleware')
        return response
class classbasedMiddleware_1:
    def __init__(self, get_response):
        self.get_response = get_response
        print('classbasedMiddleware_1 initialized')

    def __call__(self, request):
        print('Before View: classbasedMiddleware_1')
        #response = self.get_response(request)
        response = HttpResponse('Will not go to view')
        #print('After View: classbasedMiddleware_1')
        return response

class process_view_Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('process_view_Middleware initialized')

    def __call__(self, request):
        #print('Before View: process_view_Middleware')
        response = self.get_response(request)
        #response = HttpResponse('Will not go to view')
        #print('After View: classbasedMiddleware_1')
        return response
    # it is called just before the view
    def process_view(request, view_func, *args, **kwargs):
        #print('view_func', view_func)
        #return HttpResponse('Process View')
        return None

class process_exception_middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('process_exception_middleware initialized')

    def __call__(self, request):
        print('Before View: process_exception_middleware')
        response = self.get_response(request)
        #response = HttpResponse('Will not go to view')
        print('After View: process_exception_middleware')
        return response
    def process_exception(self, request, exception):
        msg = exception
        excp_class_name = exception.__class__.__name__
        return HttpResponse('{}: {}'.format(excp_class_name, msg))


class process_template_response_middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('process_template_response_middleware initialized')

    def __call__(self, request):
        print('Before View: process_template_response_middleware')
        response = self.get_response(request)
        #response = HttpResponse('Will not go to view')
        #print('After View: classbasedMiddleware_1')
        return response

    def process_template_response(self, request, response):
        response.context_data['name'] = 'process_template_response'
        return response
