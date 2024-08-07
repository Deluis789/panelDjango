from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    correo = models.EmailField(max_length=100, null=False)
    telefono = models.IntegerField(null=True)
    f_nac = models.DateField(null=True)
    f_registro = models.DateTimeField(auto_now_add=True, null=True)