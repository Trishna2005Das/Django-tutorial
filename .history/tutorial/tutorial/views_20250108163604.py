from django.http import HttpResponse
from django

def home(request):
    return HttpResponse('Hello World!')

def about(request):
    return HttpResponse('About')

def contact(request):
    return HttpResponse('Contact')