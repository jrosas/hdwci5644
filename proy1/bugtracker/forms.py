from django import forms

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
	
