from django.shortcuts import render

# Create your views here


from django.shortcuts import render_to_response

def do_it(request, n):
    n = int(n)
    test = looping(n)

    result = fib(n)
    return render_to_response('fibonacci.html', {'n': n, 'r': result, 'l': test})

def looping(n):

    list = [] 
    for x in xrange(1, n+1):
        y = fib(x)

        list.append(y) 
    return list       

def fib(n):
    if n in [0, 1]:
	return n
    else:
	return fib(n - 1) + fib(n - 2)

def index(request):
    return render(request, 'index.html')
