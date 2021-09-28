from django.test import TestCase

# Python utils
import json

# Django REST Framework
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from SICEI.models import Alumno

# Create your tests here.

class AlumnoTestCase(APITestCase):
    # Add some dummy students to test database
    def setUp(self):
        alumno = Alumno(nombre="test_alumn_1", matricula=11111111).save()
        alumno = Alumno(nombre="test_alumn_2", matricula=22222222).save()
        alumno = Alumno(nombre="test_alumn_3", matricula=33333333).save()

    def test_dummy_students_correctly_added(self):
        # Test database has exactly 3 items
        self.assertEqual(Alumno.objects.count(), 3)

    def test_get_students_list(self):

        # Get the students list
        client = APIClient()
        response = client.get("/api/alumnos/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # The response has 3 items
        self.assertEqual(len(json.loads(response.content)), 3)
        # and those 3 items are the same we added before
        self.assertEqual(json.loads(response.content), [{'nombre': 'test_alumn_1', 'matricula': 11111111},
                                                        {'nombre': 'test_alumn_2', 'matricula': 22222222},
                                                        {'nombre': 'test_alumn_3', 'matricula': 33333333}])
