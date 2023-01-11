from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def noticias(request):
    return render(request, "noticias.html")

def analisis(request):
    return render(request, "analisis.html")
    
def posteo(request):
    return render(request, "posteo.html")

def nosotros(request):
    return render(request, "nosotros.html")