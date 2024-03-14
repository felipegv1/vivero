from django.test import TestCase
from ..models import Finca, Productor
from ..views.fincaView import *


class FincaTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            documentoIdentidad='111',
            nombre='a',
            apellido='b',
            telefono='333',
            correo='a.b@test.com'
        )
        Finca.objects.create(
            productor=self.productor,
            numeroCatastro='001',
            municipioUbicacion='Pereira'
        )

    def test_finca(self):
        finca = Finca.objects.get(numeroCatastro='001')
        self.assertEqual(finca.productor, self.productor)
        self.assertEqual(finca.numeroCatastro, '001')
        self.assertEqual(finca.municipioUbicacion, 'Pereira')
