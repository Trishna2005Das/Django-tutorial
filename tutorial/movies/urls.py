
from django.urls import path
from . import views
#localhost:8000/movies
#localhost:8000/movies/
urlpatterns = [
       path('home/', views.home),
       path('<name>/<int:id>/',views.lists ),
       path('index/',views.index)
] 
