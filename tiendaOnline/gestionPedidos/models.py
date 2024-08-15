from django.db import models

# Create your models here.

class Cliente (models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    correo = models.EmailField()
    tel= models.CharField(max_length=10)
    
class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    num_pedido = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    
