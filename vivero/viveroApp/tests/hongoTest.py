import datetime
from django.test import TestCase
from ..models import Hongo, Productor, Finca, Vivero, Labor
from ..views.productoControlView import *
from django.core.exceptions import ValidationError


class HongoTestCase(TestCase):
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
        Hongo.objects.create(
            labor=self.labor,
            registroIca='123',
            nombreProducto='H1',
            frecuenciaAplicacion=15,
            valorProducto=5000,
            periodoCarencia=3,
            nombreHongo='Hongo1'
        )

    def testHongo(self):
        hongo = Hongo.objects.get(nombreProducto='H1')
        self.assertEqual(hongo.registroIca, '123')
        self.assertEqual(hongo.frecuenciaAplicacion, 15)
        self.assertEqual(hongo.valorProducto, 5000)
        self.assertEqual(hongo.periodoCarencia, 3)
        self.assertEqual(hongo.nombreHongo, 'Hongo1')

    def test_campos_obligatorios_hongo(self):
        with self.assertRaises(ValidationError):
            # Intenta registrar un Hongo sin nombre del hongo
            registrarHongo("H123", "Fungicida C", 7,
                           150, 5, '', self.labor.id)

    def test_crear_hongo(self):
        hongo = registrarHongo("H123", "Fungicida C",
                               7, 150, 5, 'A', self.labor.id)
        self.assertEqual(hongo.registroIca, "H123")
        self.assertEqual(hongo.nombreProducto, "Fungicida C")
        self.assertEqual(hongo.frecuenciaAplicacion, 7)
        self.assertEqual(hongo.valorProducto, 150)
        self.assertEqual(hongo.periodoCarencia, 5)
        self.assertEqual(hongo.nombreHongo, 'A')
