import datetime
from django.test import TestCase
from ..models import Fertilizante, Productor, Finca, Vivero, Labor
from ..views.productoControlView import *


class FertilizanteTestCase(TestCase):
    def setUp(self):
        productor = Productor.objects.create(
            documentoIdentidad='111',
            nombre='a',
            apellido='b',
            telefono='333',
            correo='a.b@test.com'
        )
        finca = Finca.objects.create(
            productor=productor,
            numeroCatastro='001',
            municipioUbicacion='Pereira'
        )
        self.vivero = Vivero.objects.create(
            finca=finca,
            codigo='v1',
            tipoCultivo='Cultivo1'
        )
        self.labor = Labor.objects.create(
            vivero=self.vivero,
            fecha=datetime.date.today(),
            descripcion='Labor1'
        )
        Fertilizante.objects.create(
            labor=self.labor,
            registroIca='123',
            nombreProducto='F1',
            frecuenciaAplicacion=45,
            valorProducto=1500,
            fechaUltimaAplicacion=datetime.date.today() - datetime.timedelta(days=15)
        )

    def test_fertilizante(self):
        fertilizante = Fertilizante.objects.get(nombreProducto='F1')
        self.assertEqual(fertilizante.registroIca, '123')
        self.assertEqual(fertilizante.frecuenciaAplicacion, 45)
        self.assertEqual(fertilizante.valorProducto, 1500)
        # Verifica que la fecha de última aplicación sea correcta teniendo en cuenta el timedelta
        expected_fecha = datetime.date.today() - datetime.timedelta(days=15)
        self.assertEqual(fertilizante.fechaUltimaAplicacion, expected_fecha)
