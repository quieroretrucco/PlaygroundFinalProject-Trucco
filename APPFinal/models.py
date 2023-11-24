from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Departamento(models.Model):
    barrio = models.CharField(max_length=40, null=True, blank=True)
    direccion = models.CharField(max_length=40)
    piso = models.IntegerField(null=True, blank=True)
    depto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="imagendepto/")

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"