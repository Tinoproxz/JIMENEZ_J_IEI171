from django.db import models
from django.core import validators


class Socios(models.Model):
    ESTADOS = [('VIGENTE', 'Vigente'), ('SUSPENDIDO', 'Suspendido'), ('RETIRADO', 'Retirado')]
    SEXO = [('MASCULINO', 'Masculino'), ('FEMENINO', 'Femenino'), ('NO BINARIO', 'No Binario')]

    nombreSocio = models.CharField(verbose_name="Nombre Socio",max_length=80,validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(80)])
    fechaIncorporacion = models.DateField(verbose_name="Fecha de Incorporacion")
    añoNacimiento = models.IntegerField(verbose_name="Año de Nacimiento",validators=[validators.MaxValueValidator(2023), validators.MinValueValidator(1923)])
    telefono = models.CharField(max_length=12,validators=[validators.MaxLengthValidator(12), validators.MinLengthValidator(9)])
    correo = models.EmailField()
    estado = models.CharField(max_length=15,choices=ESTADOS)
    sexo = models.CharField(max_length=15,choices=SEXO)
    observacion = models.CharField(max_length=250,blank=True)