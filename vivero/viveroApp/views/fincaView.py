from ..models.finca import Finca
from ..models.productor import Productor


def register_finca(productorId, numeroCatastro, municipioUbicacion):
    productor = Productor.objects.get(id=productorId)

    finca = Finca(
        productor=productorId,
        numero_catastro=numeroCatastro,
        municipioUbicacion=municipioUbicacion
    )
    finca.full_clean()
    finca.save()
    return finca
