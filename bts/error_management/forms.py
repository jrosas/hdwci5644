from django.forms.models import BaseModelFormSet
from models import ESTADO_CHOICES,Error
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class FormularioModificarError(forms.ModelForm):
	class Meta:
		model=Error
		exclude=('descripcion','prioridad','fecha_reporte','original','informacion_duplicacion','usuario_reporto','usuario_encargado','aplicacion','nombre')

class FormularioRegistrarError(forms.ModelForm):
	class Meta:
		model=Error
		exclude=('fecha_reporte','usuario_reporto','usuario_encargado')


