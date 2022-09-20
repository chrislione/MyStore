from django . shortcuts import render
from django . http import HttpResponse

# Create your views here.
# def say_hello(request):
#     return HttpResponse("hello world this is working")


def say_hello(request):
    
    return render(request,"index.html",{'name':'christian'}) #pass in 'name' at index.html file