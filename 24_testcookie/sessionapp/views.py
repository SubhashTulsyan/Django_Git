from django.shortcuts import render

# Create your views here.

def setTestCookie(request):
    request.session.set_test_cookie()
    return render(request, 'sessionapp/set.html')

def checkTestCookie(request):
    bool = request.session.test_cookie_worked()
    return render(request, 'sessionapp/get.html', {'bool': bool})

def delTestCookie(request):
    request.session.delete_test_cookie()
    return render(request, 'sessionapp/del.html')