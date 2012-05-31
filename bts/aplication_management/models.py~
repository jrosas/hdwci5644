from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Aplicacion(models.Model):
        id= models.AutoField(primary_key=True)
        nombre=models.CharField(max_length=30)
        version=models.CharField(max_length=30)
        usuario=models.ManyToManyField(User)
#class Aplicacion_Usuario(models.Model):
#        id= models.AutoField(primary_key=True)
#        aplicacion=models.ForeignKey(Aplicacion)
#        usuario=models.ForeignKey(User)
