import datetime
from django.test import TestCase
from ..models import Labor, Productor, Finca, Vivero
from ..views.laborView import *
from django.core.exceptions import ValidationError


class LaborTestCase(TestCase):
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
        Labor.objects.create(
            vivero=self.vivero,
            fecha=datetime.date.today(),
            descripcion='Labor1'
        )

    def test_labor(self):
        labor = Labor.objects.get(descripcion='Labor1')
        self.assertEqual(labor.vivero, self.vivero)
        self.assertEqual(labor.fecha, datetime.date.today())
        self.assertEqual(labor.descripcion, 'Labor1')
