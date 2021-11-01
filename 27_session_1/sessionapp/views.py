from django.shortcuts import render

# Create your views here.

def setSession(request):
    request.session['name'] = 'Subhash'
    request.session['age'] = '28'
    #request.session['gender'] = 'FF'
    request.session.set_expiry(0) # session ends once we close the browser.
    return render(request, 'sessionapp/set.html')

def getSession(request):
    #name = request.session.get('name', 'Guest')
    name = request.session['name']
    #age = request.session.get('age', '28')
    age = request.session['age']
    #gender = request.session.setdefault('gender', 'M')
    #keys = request.session.keys()
    #print(keys)
    #items = request.session.items()
    #print(items)
    ses_cookie_age = request.session.get_session_cookie_age()
    print('ses_cookie_age: ', ses_cookie_age)
    expiry_age = request.session.get_expiry_age()
    print('expiry_age: ', expiry_age)
    expiry_date = request.session.get_expiry_date()
    print('expiry_date: ', expiry_date)
    expiry_browser_close = request.session.get_expire_at_browser_close()
    print('expiry_browser_close: ', expiry_browser_close)

    val = {'name': name,
           'age': age,
           #'keys': keys,
           #'items': items,
           'ses_cookie_age': ses_cookie_age,
           'expiry_age': expiry_age,
           'expiry_date': expiry_date,
           'expiry_browser_close': expiry_browser_close,
           }
    return render(request, 'sessionapp/get.html', val)

def delSession(request):
    request.session.flush()
    request.session.clear_expired()
    # if 'name' in request.session:
    #     #del request.session['name']
    return render(request, 'sessionapp/del.html')