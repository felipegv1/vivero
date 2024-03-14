from django.test import TestCase
from ..models import Vivero, Productor, Finca, Labor
from ..views.viveroView import *
from django.core.exceptions import ValidationError


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
        self.vivero = Vivero.objects.create(
            finca=self.finca,
            codigo='v1',
            tipoCultivo='Cultivo1'
        )

        self.labor1 = Labor.objects.create(
            vivero=self.vivero,
            fecha='2024-03-14',
            descripcion='Fertilizacion'
        )

        self.labor2 = Labor.objects.create(
            vivero=self.vivero,
            fecha='2024-03-21',
            descripcion='Antifungico'
        )

    def testVivero(self):
        vivero = Vivero.objects.get(codigo='v1')
        self.assertEqual(vivero.finca, self.finca)
        self.assertEqual(vivero.codigo, 'v1')
        self.assertEqual(vivero.tipoCultivo, 'Cultivo1')

    def testCamposObligatorios(self):
        with self.assertRaises(ValidationError):
            # No tiene tipo de cultivo
            registrarVivero(1, 'v2', '')

    def testRegistrarVivero(self):
        vivero = registrarVivero(1, 'v2', 'Cultivo2')
        self.assertEqual(vivero.finca, self.finca)
        self.assertEqual(vivero.codigo, 'v2')
        self.assertEqual(vivero.tipoCultivo, 'Cultivo2')

    def testActualizarTipoCultivo(self):
        vivero = Vivero.objects.get(codigo='v1')
        actualizarTipoCultivo(vivero.id, 'CultivoTest')
        vivero.refresh_from_db()
        self.assertEqual(vivero.tipoCultivo, 'CultivoTest')

    def testListaLaboresVivero(self):
        labores = listaLaboresVivero(self.vivero.id)

        # Cantidad de labores en setUp
        self.assertEqual(labores.count(), 2)

        # Es verdadero si existen en labores del vivero
        self.assertTrue(labores.filter(id=self.labor1.id).exists())
        self.assertTrue(labores.filter(id=self.labor2.id).exists())

        # Verificar con las descripciones
        self.assertEqual(labores[0].descripcion, 'Fertilizacion')
        self.assertEqual(labores[1].descripcion, 'Antifungico')
