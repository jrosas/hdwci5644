from django.forms.models import BaseModelFormSet
from aplication_management.models import Aplicacion
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class FormularioCrearAplicacion(forms.ModelForm):
        class Meta:
                model=Aplicacion

