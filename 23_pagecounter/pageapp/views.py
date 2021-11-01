from django.shortcuts import render

# Create your views here.

def home(request):
    count = request.session.get('count', 0)
    count = count + 1
    request.session['count'] = count
    return render(request, 'pageapp/pagecounter.html', {'count': count})