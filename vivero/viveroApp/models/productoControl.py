from django.db import models
from .labor import Labor


class ProductoControl(models.Model):
    registroIca = models.CharField(max_length=100)
    nombreProducto = models.CharField(max_length=100)
    frecuenciaAplicacion = models.IntegerField()
    valorProducto = models.IntegerField()
    labor = models.ForeignKey(
        Labor, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Hongo(ProductoControl):
    periodoCarencia = models.IntegerField()
    nombreHongo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_hongo


class Plaga(ProductoControl):
    periodoCarencia = models.IntegerField()

    def __str__(self):
        return self.nombre_producto


class Fertilizante(ProductoControl):
    fechaUltimaAplicacion = models.DateField()

    def __str__(self):
        return self.nombre_producto
