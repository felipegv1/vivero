from django.test import TestCase
from ..models import Finca, Productor, Vivero
from ..views.fincaView import *
from django.core.exceptions import ValidationError


class FincaTestCase(TestCase):
    def setUp(self):
        self.productor = Productor.objects.create(
            documentoIdentidad='111',
            nombre='a',
            apellido='b',
            telefono='333',
            correo='a.b@test.com'
        )
        self.finca = Finca.objects.create(
            productor=self.productor,
            numeroCatastro='001',
            municipioUbicacion='Pereira'
        )
        self.vivero1 = Vivero.objects.create(
            finca=self.finca,
            codigo='V1',
            tipoCultivo='Cultivo1'
        )
        self.vivero2 = Vivero.objects.create(
            finca=self.finca,
            codigo='V2',
            tipoCultivo='Cultivo2'
        )

    def testFinca(self):
        finca = Finca.objects.get(numeroCatastro='001')
        self.assertEqual(finca.productor, self.productor)
        self.assertEqual(finca.numeroCatastro, '001')
        self.assertEqual(finca.municipioUbicacion, 'Pereira')

    def testCamposObligatorios(self):
        with self.assertRaises(ValidationError):
            # No tiene asignado un municipio
            registrarFinca(1, "002", "")

    def testRegistrarFinca(self):
        finca = registrarFinca(1, '003', 'Dosquebradas')
        self.assertEqual(finca.productor, self.productor)
        self.assertEqual(finca.numeroCatastro, '003')
        self.assertEqual(finca.municipioUbicacion, 'Dosquebradas')

    def testObtenerViverosFinca(self):
        finca = Finca.objects.get(numeroCatastro='001')
        viveros = obtenerViverosFinca(finca.id)
        self.assertIn(self.vivero1, viveros)
        self.assertIn(self.vivero2, viveros)
        self.assertEqual(viveros.count(), 2)

    def testEliminarFinca(self):
        idFinca = self.finca.id
        eliminarFinca(idFinca)
        # assertTrue(expr)/assertFalse(expr) .exist devuelve verdadero o false
        self.assertFalse(Finca.objects.filter(id=idFinca).exists())
