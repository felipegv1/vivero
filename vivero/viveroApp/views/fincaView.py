from ..models.finca import Finca
from ..models.productor import Productor


def registrarFinca(productorId, numeroCatastro, municipioUbicacion):
    productor = Productor.objects.get(id=productorId)

    finca = Finca(
        productor=productor,
        numeroCatastro=numeroCatastro,
        municipioUbicacion=municipioUbicacion
    )
    finca.full_clean()
    finca.save()
    return finca


def obtenerViverosFinca(idFinca):
    finca = Finca.objects.get(id=idFinca)
    return finca.vivero_set.all()


def eliminarFinca(idFinca):
    finca = Finca.objects.get(id=idFinca)
    finca.delete()
    return finca
