from django.shortcuts import render
from datetime import datetime
# Create your views here.

def home(request):
    a = 'apple'
    b = 'ball'
    c = 'cat'
    but = 'butterfly'
    test = '<p>fbksbksbskgs</p>'
    dt = datetime.now()
    no = 1234.6755864774854

    dc = {'names':{'name1': 'Mohan', 'name2': 'Sohan'}, 'Roll':21}
    dict_1 = {'a': a, 'b': b, 'c': c, 'but': but, 'test': test, 'dt': dt, 'no': no, 'dc':dc}
    return render(request, 'app1/home.html', context=dict_1)