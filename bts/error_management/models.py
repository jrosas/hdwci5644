from django.db import models
from django.contrib.auth.models import User
from aplication_management.models import Aplicacion

# Create your models here.

ESTADO_CHOICES = (
        ('S','Sin Confirmar'),
        ('A','Asignado'),
        ('R','Resuelto'),
        ('D','Duplicado'),
        ('C','Cerrado'),
)

PRIORIDAD_CHOICES = (
        ('B','Baja'),
        ('M','Media'),
        ('A','Alta'),
)


def get_sentinel_user():
        return User.objects.get_or_create(username='deleted')[0]

class Error(models.Model):
        
        id= models.AutoField(primary_key=True)
        estado= models.CharField(max_length=1, choices=ESTADO_CHOICES)
        prioridad=models.CharField(max_length=1, choices=PRIORIDAD_CHOICES)
        fecha_reporte=models.DateField(auto_now_add=True)
        original=models.BooleanField()
	nombre=models.CharField(max_length=30)
        descripcion=models.TextField(max_length=4000)
	informacion_duplicacion=models.TextField(max_length=4000)
        usuario_reporto=models.ForeignKey(User,related_name='+',on_delete=models.SET(get_sentinel_user))
        usuario_encargado=models.ForeignKey(User,related_name='+', on_delete=models.SET(get_sentinel_user))
        aplicacion=models.ForeignKey(Aplicacion)
        fecha_modificacion=models.DateField(auto_now=True)
