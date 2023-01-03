from django.urls import path
from Web_Blog.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('noticias/', noticias, name="noticias"),
    path('analisis/', analisis, name= "analisis"),
    path('experiencias/', experiencias, name="experiencias"),
    path('posteo/', posteo, name="posteo"),
    path('nosotros/', nosotros, name="nosotros"),
]