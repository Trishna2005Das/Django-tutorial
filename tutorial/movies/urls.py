
from django.urls import path
from . import views
#localhost:8000/movies
#localhost:8000/movies/
urlpatterns = [
       path('', views.index, name='index'),
       
    
    
] 