from django.test import TestCase
from ..models import Productor
from ..views.productorView import registrarProductor


class ProductorTestCase(TestCase):
    def testCrearProductor(self):
        productor = registrarProductor("123456789", "Juan", "Perez",
                                       "1234567890", "juan@example.com")
        self.assertEqual(productor.documentoIdentidad, "123456789")
        self.assertEqual(productor.nombre, "Juan")
        self.assertEqual(productor.apellido, "Perez")
        self.assertEqual(productor.telefono, "1234567890")
        self.assertEqual(productor.correo, "juan@example.com")
