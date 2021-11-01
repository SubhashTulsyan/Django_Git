from django.http.response import HttpResponse
from django.shortcuts import render
from . import signals
# Create your views here.
def home(request):
    signals.send_coupon.send(sender = None, request = request)
    return HttpResponse('OK')