import datetime
from django.test import TestCase
from ..models import Plaga, Productor, Finca, Vivero, Labor
from ..views.productoControlView import *
from django.core.exceptions import ValidationError


class PlagaTestCase(TestCase):
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
        Plaga.objects.create(
            labor=self.labor,
            registroIca='123',
            nombreProducto='P1',
            frecuenciaAplicacion=30,
            valorProducto=2000,
            periodoCarencia=7
        )

    def testPlaga(self):
        plaga = Plaga.objects.get(nombreProducto='P1')
        self.assertEqual(plaga.registroIca, '123')
        self.assertEqual(plaga.frecuenciaAplicacion, 30)
        self.assertEqual(plaga.valorProducto, 2000)
        self.assertEqual(plaga.periodoCarencia, 7)
