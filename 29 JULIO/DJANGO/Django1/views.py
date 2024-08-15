from django.http import HttpResponse

def holaMundo(request): #Cada función representa una vista
    return HttpResponse ("HOLA MUNDO, ESTA ES LA PRIMERA VISTA EN PYTHON")


def adiosMundo(request):
    return HttpResponse ("CON ESTA ME DESPIDO")

def verEdad(request, edad, anio):
    periodo = anio - 2024
    edad = edad + periodo
    
    doc = f"""
    <html>
    <body>
    <h1>
    En {anio} usted tendrá {edad} años
    </h1>
    </body>
    </html>
    """
    return HttpResponse(doc)
    


