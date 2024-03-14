from ..models.vivero import Vivero
from ..models.finca import Finca


def registrarVivero(idFinca, codigo, tipoCultivo):
    finca = Finca.objects.get(id=idFinca)
    vivero = Vivero(
        finca=finca,
        codigo=codigo,
        tipoCultivo=tipoCultivo
    )
    vivero.full_clean()
    vivero.save()
    return vivero


def actualizarTipoCultivo(idVivero, nuevoTipoCultivo):
    vivero = Vivero.objects.get(id=idVivero)
    vivero.tipoCultivo = nuevoTipoCultivo
    vivero.full_clean()
    vivero.save()
    return vivero


def listaLaboresVivero(idVivero):
    vivero = Vivero.objects.get(id=idVivero)
    return vivero.labor_set.all()

