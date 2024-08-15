from django.contrib import admin
from gestionPedidos.models import Articulo, Cliente, Pedido

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("nombre", "seccion", "precio")
    list_filter = ("seccion",)
    search_fields =("nombre", "seccion")
    

# Register your models here.
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Cliente)
admin.site.register(Pedido)

