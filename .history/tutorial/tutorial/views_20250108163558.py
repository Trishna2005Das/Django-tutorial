from django.http import HttpResponse
from 

def home(request):
    return HttpResponse('Hello World!')

def about(request):
    return HttpResponse('About')

def contact(request):
    return HttpResponse('Contact')