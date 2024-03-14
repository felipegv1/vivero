from ..models.productor import Productor
from ..models.finca import Finca


def registrarProductor(documentoIdentidad, nombre, apellido, telefono, correo):
    productor = Productor.objects.create(
        documentoIdentidad=documentoIdentidad,
        nombre=nombre,
        apellido=apellido,
        telefono=telefono,
        correo=correo
    )
    return productor


def agregarFincaAProductor(productorId, numeroCatastro, municipioUbicacion):
    productor = Productor.objects.get(id=productorId)
    finca = Finca.objects.create(
        productor=productor,
        numero_catastro=numeroCatastro,
        municipio_ubicacion=municipioUbicacion
    )
    return finca


def getViverosProductor(productor_id):
    fincas = Finca.objects.filter(productor_id=productor_id)
    viveros_list = [finca.viveros.all() for finca in fincas]
    viveros = [vivero for sublist in viveros_list for vivero in sublist]
    return viveros
