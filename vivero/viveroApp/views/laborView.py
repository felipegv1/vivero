from ..models.labor import Labor
from ..models.vivero import Vivero
from ..models.productoControl import *


def registrarLabor(idVivero, fecha, descripcion):
    vivero = Vivero.objects.get(id=idVivero)
    labor = Labor(
        vivero=vivero,
        fecha=fecha,
        descripcion=descripcion
    )
    labor.full_clean()
    labor.save()
    return labor


def actualizarLabor(idLabor, fecha=None, descripcion=None):
    labor = Labor.objects.get(id=idLabor)
    if fecha != None:
        labor.fecha = fecha
    if descripcion != None:
        labor.descripcion = descripcion
    labor.full_clean()
    labor.save()
    return labor


def filtroProductoControlLabor(idLabor, productoControl):
    labor = Labor.objects.get(id=idLabor)
    if productoControl == 'hongo':
        productos = labor.hongo_set.all()
    elif productoControl == 'fertilizante':
        productos = labor.fertilizante_set.all()
    elif productoControl == 'plaga':
        productos = labor.plaga_set.all()
    else:
        raise ValueError("Tipo de producto de control no válido")
    return productos
