from django.http import HttpResponse
from django.shortcuts import render

from gestionPedidos.models import Articulo

# Create your views here.
def buscar_arts(request):
    return render(request, "buscar_art.html")

def buscar(request):
    if(request.GET['art']):
        #mensaje = f"Articulo buscado: {request.GET['art']}"
        articulo = request.GET['art']
        
        if(len(articulo) > 20):
            mensaje = "Nombre de Artículo muy largo"
        else:
            articulos = Articulo.objects.filter(nombre__icontains = articulo)
            return render(request, "resultado_busqueda.html", {"arts": articulos, "art": articulo})
            
    else:
        mensaje = "No ha especificado un Artículo" 
        
    return HttpResponse(mensaje)

    
    