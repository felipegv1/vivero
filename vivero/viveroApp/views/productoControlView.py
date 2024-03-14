from ..models.productoControl import *
from ..models.labor import Labor


def registrarHongo(registroIca, nombreProducto, frecuenciaAplicacion, valorProducto, periodoCarencia, nombreHongo, idLabor):
    labor = Labor.objects.get(id=idLabor)
    hongo = Hongo(
        registroIca=registroIca,
        nombreProducto=nombreProducto,
        frecuenciaAplicacion=frecuenciaAplicacion,
        valorProducto=valorProducto,
        periodoCarencia=periodoCarencia,
        nombreHongo=nombreHongo,
        labor=labor
    )
    hongo.full_clean()
    hongo.save()
    return hongo


def registrarPlaga(registroIca, nombreProducto, frecuenciaAplicacion, valorProducto, periodoCarencia, idLabor):
    labor = Labor.objects.get(id=idLabor)
    plaga = Plaga(
        registroIca=registroIca,
        nombreProducto=nombreProducto,
        frecuenciaAplicacion=frecuenciaAplicacion,
        valorProducto=valorProducto,
        periodoCarencia=periodoCarencia,
        labor=labor
    )
    plaga.full_clean()
    plaga.save()
    return plaga


def registrarFertilizante(registroIca, nombreProducto, frecuenciaAplicacion, valorProducto, fechaUltimaAplicacion, idLabor):
    labor = Labor.objects.get(id=idLabor)
    fertilizante = Fertilizante(
        registroIca=registroIca,
        nombreProducto=nombreProducto,
        frecuenciaAplicacion=frecuenciaAplicacion,
        valorProducto=valorProducto,
        fechaUltimaAplicacion=fechaUltimaAplicacion,
        labor=labor
    )
    fertilizante.full_clean()
    fertilizante.save()
    return fertilizante
