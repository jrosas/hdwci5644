from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def get_sentinel_user():
        return User.objects.get_or_create(username='deleted')[0]

class Mensaje(models.Model):
	id_m= models.AutoField(primary_key=True)
        emisor=models.ForeignKey(User,related_name='+',on_delete=models.SET(get_sentinel_user))
        receptor=models.ForeignKey(User,related_name='+',on_delete=models.SET(get_sentinel_user))
	asunto=models.CharField(max_length=30)
	contenido=models.TextField(max_length=4000)
