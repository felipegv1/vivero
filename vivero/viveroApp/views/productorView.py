from ..models.productor import Productor
from ..models.finca import Finca


def registrarProductor(documentoIdentidad, nombre, apellido, telefono, correo):
    productor = Productor(
        documentoIdentidad=documentoIdentidad,
        nombre=nombre,
        apellido=apellido,
        telefono=telefono,
        correo=correo
    )
    productor.full_clean()
    productor.save()
    return productor


def agregarFincaAProductor(productorId, numeroCatastro, municipioUbicacion):
    productor = Productor.objects.get(id=productorId)
    finca = Finca.objects.create(
        productor=productor,
        numeroCatastro=numeroCatastro,
        municipioUbicacion=municipioUbicacion
    )
    return finca


def actualizarProductor(id, nombre=None, apellido=None, telefono=None, correo=None):
    productor = Productor.objects.get(id=id)
    if nombre:
        productor.nombre = nombre
    if apellido:
        productor.apellido = apellido
    if telefono:
        productor.telefono = telefono
    if correo:
        productor.correo = correo
    productor.save()
    return productor


def getViverosProductor(productor_id):
    fincas = Finca.objects.filter(productor_id=productor_id)
    viveros_list = [finca.viveros.all() for finca in fincas]
    viveros = [vivero for sublist in viveros_list for vivero in sublist]
    return viveros
