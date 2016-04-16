from django.shortcuts import render












# Create your views here.

from django.shortcuts import render_to_response

def say(request, name):
    return render_to_response('hello.html', {'name': name}) 
