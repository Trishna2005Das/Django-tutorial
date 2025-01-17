from django.http import HttpResponse
from django.shortcuts import render
#views handle the requests and return the response
#when user visits the website home/ then we want the use to see the home page and views comes between url and response part.
#there are two tyoes of veiws 1. Class based view 2. Function based view

#fbv-function based view
#the request parameter can be named anything but by convention it is request beacuse it denotes the incoming http request.it is an instance of httprequest class.
def home(request):
    #return HttpResponse('Hello World!')
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse('About')
    

def contact(request):
    return HttpResponse('Contact')