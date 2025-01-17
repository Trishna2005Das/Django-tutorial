from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('Hello World!')
  
def lists(request,name,id):
    print(type(id))
    return HttpResponse( f'{name} {id}')

#path convertors->str,int 

def index(request):
    return render(request,'movies/index.html')