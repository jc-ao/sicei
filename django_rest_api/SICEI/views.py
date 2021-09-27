from django.shortcuts import render

# Modules for REST APIs
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from SICEI.models import Alumno
from SICEI.serializers import AlumnoSerializer


# Create your views here.

class AlumnoList(APIView):
    """
    List all alumns.
    """
    def get(self, request, format=None):
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)

