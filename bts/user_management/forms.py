from django.forms.models import BaseModelFormSet
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class FormularioRegistro(forms.Form):
        username = forms.CharField(max_length=20)
        nombre = forms.CharField(max_length=20)
        apellido = forms.CharField(max_length=20)
        correo = forms.EmailField()
        password = forms.CharField(max_length=20, widget=forms.PasswordInput)
        confirm = forms.CharField(max_length=20, widget=forms.PasswordInput)

class FormularioModificarUser(forms.Form):
        nombre = forms.CharField(max_length=20, required=False)
        apellido = forms.CharField(max_length=20, required=False)
        correo = forms.EmailField(required=False)
        password = forms.CharField(max_length=20,required=False, widget=forms.PasswordInput)
        confirm = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput)

class FormularioUsuarioAd(forms.ModelForm):
        username = forms.CharField(help_text='')
        active=forms.BooleanField(help_text='')
        superuser_status=forms.BooleanField(help_text='')
        staff_status=forms.BooleanField(help_text='')
        class Meta:
                model=User
                fields=('username','first_name','last_name','email','password','active','superuser_status','staff_status','groups','last_login','user_permissions','date_joined')


