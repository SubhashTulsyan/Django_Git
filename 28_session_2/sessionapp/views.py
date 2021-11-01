from django.shortcuts import render

# Create your views here.

def setSession(request):
    request.session['name'] = 'Subhash'
    return render(request, 'sessionapp/set.html')

def getSession(request):
    name = request.session['name']
    # ses_cookie_age = request.session.get_session_cookie_age()
    # print('ses_cookie_age: ', ses_cookie_age)
    # expiry_age = request.session.get_expiry_age()
    # print('expiry_age: ', expiry_age)
    # expiry_date = request.session.get_expiry_date()
    # print('expiry_date: ', expiry_date)
    # expiry_browser_close = request.session.get_expire_at_browser_close()
    # print('expiry_browser_close: ', expiry_browser_close)
    return render(request, 'sessionapp/get.html', {'name': name})

def delSession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'sessionapp/del.html')