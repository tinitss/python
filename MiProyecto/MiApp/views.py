from django.shortcuts import render, HttpResponse
from ServApp.models import Servicio

# Create your views here.

def inicio(request):
    return render(request, "MiApp/inicio.html")

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "MiApp/servicios.html", {'servicios': servicios})

def tienda(request):
    return render(request, "MiApp/tienda.html")

def blog(request):
    return render(request, "MiApp/blog.html")

def contacto(request):
    return render(request, "MiApp/contacto.html")