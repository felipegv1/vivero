from django.test import TestCase  # unittest.TestCase
from ..models import Productor
from ..views.productorView import *
from django.core.exceptions import ValidationError


class ProductorTestCase(TestCase):
    def setUp(self):
        Productor.objects.create(
            documentoIdentidad='111',
            nombre='a',
            apellido='b',
            telefono='333',
            correo='a.b@test.com'
        )

    def testProductor(self):
        productor = Productor.objects.get(documentoIdentidad='111')
        self.assertEqual(productor.documentoIdentidad, '111')
        self.assertEqual(productor.nombre, 'a')
        self.assertEqual(productor.apellido, 'b')
        self.assertEqual(productor.telefono, '333')
        self.assertEqual(productor.correo, 'a.b@test.com')

    # with self.assertRaises(SomeException):
        # do_something()
    def testCamposObligatorios(self):
        with self.assertRaises(ValidationError):
            registrarProductor("", "Test", "Apellido",
                                           "123", "Test@test.com")  # No tiene documento de identidad

    def testCrearProductor(self):
        productor = registrarProductor("123456789", "Test", "Apellido",
                                       "123", "Test@test.com")
        self.assertEqual(productor.documentoIdentidad, "123456789")
        self.assertEqual(productor.nombre, "Test")
        self.assertEqual(productor.apellido, "Apellido")
        self.assertEqual(productor.telefono, "123")
        self.assertEqual(productor.correo, "Test@test.com")

    def testAgregarFincaAProductor(self):

        productor = Productor.objects.get(documentoIdentidad='111')
        numeroCatastro = "123"
        municipioUbicacion = 'Pereira'
        # Agrega finca
        agregarFinca = agregarFincaAProductor(
            productor.id, numeroCatastro, municipioUbicacion)
        # Obtiene a la finca desde la relacion con productor
        finca = productor.finca_set.get(numeroCatastro=numeroCatastro)
        # finca es miembro de productor, assertIn(member, container) Test that member is (or is not) in container.
        self.assertIn(finca, productor.finca_set.all())
        self.assertEqual(agregarFinca.numeroCatastro, finca.numeroCatastro)
        self.assertEqual(agregarFinca.municipioUbicacion,
                         finca.municipioUbicacion)

    def testActualizarProductor(self):
        productor = Productor.objects.get(documentoIdentidad='111')
        actualizarNombre = 'TestNombre'
        self.assertNotEqual(productor.nombre, actualizarNombre)
        actualizarProductor(
            productor.id,
            nombre=actualizarNombre,
        )
        productor = Productor.objects.get(documentoIdentidad='111')
        self.assertEqual(productor.nombre, actualizarNombre)
        self.assertEqual(productor.apellido, 'b')
