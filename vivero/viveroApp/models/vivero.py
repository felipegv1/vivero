from django.db import models
from .finca import Finca


class Vivero(models.Model):
    finca = models.ForeignKey(
        Finca, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=100)
    tipoCultivo = models.CharField(max_length=100)
