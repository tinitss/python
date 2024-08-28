from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "MiApp/inicio.html")

def servicios(request):
    return render(request, "MiApp/servicios.html")

def tienda(request):
    return render(request, "MiApp/tienda.html")

def blog(request):
    return render(request, "MiApp/blog.html")

def contacto(request):
    return render(request, "MiApp/contacto.html")