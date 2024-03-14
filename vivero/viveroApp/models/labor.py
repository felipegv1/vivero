from django.db import models
from .vivero import Vivero


class Labor(models.Model):
    vivero = models.ForeignKey(
        Vivero, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.TextField()
