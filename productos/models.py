from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=255) #charfiel es una cadena de texto limitada

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField() # numero entero
    puntaje = models.FloatField() # numero flotante
    
    # CASCADE: elimina el producto si se elimina la categoria
    # PROTECT: lanza error, no deja eliminar categoria
    # RESTRICT: solo deja eliminar categoria si existen productos
    # SET_NULL: convierte a null a categoria
    # SET_DEFAULT: asigna valor por defecto y nosotros se lo definimos
    Categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE
    )
# creamos relacion entre producto y categoria
