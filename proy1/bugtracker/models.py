from django.db import models

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

class Error(models.Model):
	
	id= models.AutoField(primary_key=True)
	estado= models.CharField(max_length=1, choices=ESTADO_CHOICES)
	prioridad=models.CharField(max_length=1, choices=PRIORIDAD_CHOICES)
	fecha_reporte=models.DateField()
	original=models.BooleanField()
	informacion_duplicacion=models.TextField(max_length=4000)
        usuario_reporto=models.ForeignKey(User,on_delete=models.SET(get_sentinel_user))
	usuario_encargado=models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
	fecha_modificacion=models.DateField(auto_now=True)

class ComenRep(models.Model):
	modo= models.CharField(max_length=1, choices=MODO_CHOICES)
        usuario=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
	id_error=models.ForeignKey(Error,null=False)
	contenido=models.TextField(max_length=4000)
	fecha_com=models.DateField(auto_now_add=True)

class Mensaje(models.Model):
	id_m= models.AutoField(primary_key=True)
        emisor=models.ForeignKey(User,on_delete=models.SET(get_sentinel_user))
        receptor=models.ForeignKey(User,on_delete=models.SET(get_sentinel_user))
	asunto=models.CharField(max_length=30)
	contenido=models.TextField(max_length=4000)
