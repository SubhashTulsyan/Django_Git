from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def setSession(request):
    request.session['name'] = 'Subhash'
    request.session.set_expiry(None)
    return render(request, 'sessionapp/set.html')

def getSession(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True
        return render(request, 'sessionapp/get.html', {'name': name})
    else:
        return HttpResponse('Your session has expired............')

def delSession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'sessionapp/del.html')