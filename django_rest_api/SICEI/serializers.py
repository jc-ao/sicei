from rest_framework import serializers
from SICEI.models import Alumno

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['nombre', 'matricula']