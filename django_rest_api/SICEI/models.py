from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    matricula = models.IntegerField(unique=True, blank=False)

    class Meta:
        ordering = ['pk']