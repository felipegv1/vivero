import datetime
from django.test import TestCase
from ..models import Labor, Productor, Finca, Vivero
from ..views.laborView import *
from django.core.exceptions import ValidationError


class LaborTestCase(TestCase):
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
        self.vivero = Vivero.objects.create(
            finca=self.finca,
            codigo='v1',
            tipoCultivo='Cultivo1'
        )
        self.labor = Labor.objects.create(
            vivero=self.vivero,
            fecha=datetime.date.today(),
            descripcion='Aplicacion fertilizante'
        )
        self.hongo1 = Hongo.objects.create(
            labor=self.labor,
            registroIca='123',
            nombreProducto='H1',
            frecuenciaAplicacion=15,
            valorProducto=5000,
            periodoCarencia=3,
            nombreHongo='Hongo1'
        )
        self.hongo2 = Hongo.objects.create(
            labor=self.labor,
            registroIca='321',
            nombreProducto='H2',
            frecuenciaAplicacion=15,
            valorProducto=5000,
            periodoCarencia=3,
            nombreHongo='Hongo2'
        )
        self.plaga = Plaga.objects.create(
            labor=self.labor,
            registroIca='312',
            nombreProducto='P1',
            frecuenciaAplicacion=30,
            valorProducto=2000,
            periodoCarencia=7
        )
        self.fertilizante = Fertilizante.objects.create(
            labor=self.labor,
            registroIca='231',
            nombreProducto='F1',
            frecuenciaAplicacion=45,
            valorProducto=1500,
            fechaUltimaAplicacion=datetime.date.today() - datetime.timedelta(days=15)
        )

    def testLabor(self):
        labor = Labor.objects.get(descripcion='Aplicacion fertilizante')
        self.assertEqual(labor.vivero, self.vivero)
        self.assertEqual(labor.fecha, datetime.date.today())
        self.assertEqual(labor.descripcion, 'Aplicacion fertilizante')

    def testCamposObligatorios(self):
        with self.assertRaises(ValidationError):
            # No tiene descripcion
            registrarLabor(1, datetime.date.today(), '')

    def testRegistar(self):
        labor = registrarLabor(1, datetime.date.today(), 'Control de plaga')
        self.assertEqual(labor.vivero, self.vivero)
        self.assertEqual(labor.fecha, datetime.date.today())
        self.assertEqual(labor.descripcion, 'Control de plaga')

    def testActualizarLabor(self):
        labor = Labor.objects.get(id=1)
        self.assertEqual(labor.descripcion, 'Aplicacion fertilizante')
        actualizarLabor(labor.id,
                        descripcion='Aplicacion Antifungico')
        labor.refresh_from_db()
        self.assertEqual(labor.descripcion, 'Aplicacion Antifungico')

    def testfiltroProductoControlLabor(self):
        labor = Labor.objects.get(id=1)
        controlHongos = filtroProductoControlLabor(labor.id, 'hongo')
        laborHongos = labor.hongo_set.all()
        self.assertTrue(controlHongos.exists())
        self.assertEqual(controlHongos.count(), 2)
        for hongo in controlHongos:
            self.assertIn(hongo, laborHongos)
