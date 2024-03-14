from django.db import models
from .productor import Productor


class Finca(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    numeroCatastro = models.CharField(max_length=100)
    municipioUbicacion = models.CharField(max_length=100)
