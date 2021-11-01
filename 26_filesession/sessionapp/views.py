from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def setSession(request):
    request.session['name'] = 'Subhash'
    return render(request, 'sessionapp/set.html')

def getSession(request):
    name = request.session['name']
    return render(request, 'sessionapp/get.html', {'name': name})

def delSession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'sessionapp/del.html')