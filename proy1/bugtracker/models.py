from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ESTADO_CHOICES = (
	('S','Sin Confirmar'),
	('A','Asignado'),
	('R','Resuelto'),
	('D','Duplicado'),
	('C','Cerrado'),
)

MODO_CHOICES = (
	('C','Comentario'),
	('R','Reporte'),
)

PRIORIDAD_CHOICES = (
	('B','Baja'),
	('M','Media'),
	('A','Alta'),
)

def get_sentinel_user():
	return User.objects.get_or_create(username='deleted')[0]

class Aplicacion(models.Model):
	id= models.AutoField(primary_key=True)
	nombre=models.CharField(max_length=30)
	version=models.CharField(max_length=30)


class Error(models.Model):
	
	id= models.AutoField(primary_key=True)
	estado= models.CharField(max_length=1, choices=ESTADO_CHOICES)
	prioridad=models.CharField(max_length=1, choices=PRIORIDAD_CHOICES)
	fecha_reporte=models.DateField()
	original=models.BooleanField()
	informacion_duplicacion=models.TextField(max_length=4000)
        usuario_reporto=models.ForeignKey(User,related_name='+',on_delete=models.SET(get_sentinel_user))
	usuario_encargado=models.ForeignKey(User,related_name='+', on_delete=models.SET(get_sentinel_user))
	aplicacion=models.ForeignKey(Aplicacion, related_name='+')
	fecha_modificacion=models.DateField(auto_now=True)


class Aplicacion_Usuario(models.Model):
	id= models.AutoField(primary_key=True)
	aplicacion=models.ForeignKey(Aplicacion)
	usuario=models.ForeignKey(User)

class ComenRep(models.Model):
	modo= models.CharField(max_length=1, choices=MODO_CHOICES)
        usuario=models.ForeignKey(User,related_name='+',on_delete=models.SET(get_sentinel_user))
	id_error=models.ForeignKey(Error,null=False)
	contenido=models.TextField(max_length=4000)
	fecha_com=models.DateField(auto_now_add=True)

class Mensaje(models.Model):
	id_m= models.AutoField(primary_key=True)
        emisor=models.ForeignKey(User,related_name='+',on_delete=models.SET(get_sentinel_user))
        receptor=models.ForeignKey(User,related_name='+',on_delete=models.SET(get_sentinel_user))
	asunto=models.CharField(max_length=30)
	contenido=models.TextField(max_length=4000)
