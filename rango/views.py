from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")
    context_dict={'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}
    returnrender(request,'rango/index.html', context=context_dict)
def about(request): 
    return HttpResponse("Rango says here is the about page <a href='/rango/'>index</a>") 
