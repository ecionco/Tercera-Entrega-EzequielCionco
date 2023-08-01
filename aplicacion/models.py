from django.db import models
from django.utils import timezone
# Create your models here.

class Trabajo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    requisitos_excluyentes = models.TextField()
    requisitos_no_excluyentes = models.TextField()
    salario_ofrecido = models.DecimalField(max_digits=10, decimal_places=2)

class Solicitante(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    habilidades = models.TextField()

class Vinculacion(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    job_solicitante = models.ForeignKey(Solicitante, on_delete=models.CASCADE)
    fecha_vinculacion = models.DateField(default=timezone.now)
    estado = models.CharField(max_length=50)
    salario_esperado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)
