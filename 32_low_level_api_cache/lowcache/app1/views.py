from django.shortcuts import render
from django.core.cache import cache
# Create your views here.


# cache.set(key, value, timeout=DEFAULT_TIMEOUT, version=None)
# cache.get(key, default=None, version=None)
# cache.get('my_key', 'has expired')
# cache.add(key, value, timeout=DEFAULT_TIMEOUT, version=None)
# cache.get_or_set(key, default, timeout=DEFAULT_TIMEOUT, version=None)
# cache.get_many(keys, version=None)
# cache.set_many(dict, timeout)
# cache.delete(key, version=None)
# cache.delete_many(keys, version=None)
# cache.clear()
# cache.touch(key, timeout=DEFAULT_TIMEOUT, version=None)
# cache.incr(key, delta=1, version=None)
# cache.decr(key, delta=1, version=None)
# cache.close()
def home(request):
    name = cache.get('name', 'has_expired')
    if name is 'has_expired':
        cache.set('name','a',10)
        cache.get_or_set('age', 21, 10)
    # name = cache.get('name')
    # age = cache.get('age')
    cache.clear()
    lst = cache.get_many(['name','age'], version=None)
    
    return render(request, 'app1/home.html', lst)