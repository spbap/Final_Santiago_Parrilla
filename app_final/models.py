from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    persona = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    fecha_pedido = models.DateField()
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f'Pedido de {self.persona} para {self.producto}'
