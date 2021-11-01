from django.http import response
from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.

def setCookie(request):
    response = render(request, 'cookieApp/set.html')
    response.set_cookie('name', 'Subhash', expires=datetime.utcnow()+timedelta(days=2))
    #response.set_signed_cookie('name', 'Signed_Subhash', salt='123')
    return response

def getCookie(request):
    #name = request.COOKIES.get('name', 'Guest !!')
    name = request.get_signed_cookie('name', 'Guest (if salt not matched) !!', salt = '123')
    return render(request, 'cookieApp/get.html', {'name': name})

def delCookie(request):
    response = render(request, 'cookieApp/del.html')
    response.delete_cookie('name')
    return response