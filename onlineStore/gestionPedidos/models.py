from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direcccion = models.CharField(max_length=50)
    email = models.EmailField()
    movil = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre
    
    
class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField()
    
    
class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
     