from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
#views handle the requests and return the response
#when user visits the website home/ then we want the use to see the home page and views comes between url and response part.
#there are two tyoes of veiws 1. Class based view 2. Function based view

#fbv-function based view
#the request parameter can be named anything but by convention it is request beacuse it denotes the incoming http request.it is an instance of httprequest class.

views = [
    {
        "id": 1,
        "title": "Introduction to Views",
        "content": "Views handle the requests and return the response. When a user visits the website 'home/', they see the home page. Views act as the intermediary between the URL and the response."
    },
    {
        "id": 2,
        "title": "Types of Views",
        "content": "There are two types of views: 1. Class-based views 2. Function-based views."
    },
    {
        "id": 3,
        "title": "Function-based Views (FBV)",
        "content": "The request parameter in function-based views can be named anything, but by convention, it is named 'request' as it denotes the incoming HTTP request. It is an instance of the HttpRequest class."
    }
]

def django(request):
    html = " "
    for docs in views:
        html+=f'''
          <div>
          <a href="/{docs['id']}"> 
            <h1>{docs['id']} {docs['title']} </h1></a>
            <p>{docs['content']}</p>
          </div>'''
    return HttpResponse(html)
 
def google(request):
    return HttpResponseRedirect("https://www.google.com")