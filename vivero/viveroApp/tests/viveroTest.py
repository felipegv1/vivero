from django.test import TestCase
from ..models import Vivero, Productor, Finca
from ..views.viveroView import *


class ViveroTestCase(TestCase):
    def setUp(self):
        productor = Productor.objects.create(
            documentoIdentidad='111',
            nombre='a',
            apellido='b',
            telefono='333',
            correo='a.b@test.com'
        )
        self.finca = Finca.objects.create(
            productor=productor,
            numeroCatastro='001',
            municipioUbicacion='Pereira'
        )
        Vivero.objects.create(
            finca=self.finca,
            codigo='v1',
            tipoCultivo='Cultivo1'
        )

    def test_vivero(self):
        vivero = Vivero.objects.get(codigo='v1')
        self.assertEqual(vivero.finca, self.finca)
        self.assertEqual(vivero.codigo, 'v1')
        self.assertEqual(vivero.tipoCultivo, 'Cultivo1')
