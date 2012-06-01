from django.forms.models import BaseModelFormSet
from message_management.models import Mensaje
from django import forms
from django.forms import ModelForm

class FormularioEnviarMensaje(forms.ModelForm):
        class Meta:
                model=Mensaje

