from django.contrib.auth.forms import UserChangeForm
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template import Context, loader
from django.contrib.auth.models import User, Group, Permission
from django.http import HttpResponse
from django.conf import settings
from forms import FormularioRegistro, FormularioModificarUser,FormularioUsuarioAd



def log_in(request):
        state=''
        if request.POST:
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                        if user.is_active:
                                login(request,user)
                                state='Bienvenido '+user.username
                        else:
                                state='Usuario Inactivo'
                else:
			state='Datos Invalidos'
	return render_to_response("login.html" , {'state':state} ,context_instance=RequestContext(request)) 

def logouts(request):
	logout(request)



def registrarse(request):
	
        if request.method == "GET": # Metodo GET, se va a registrar.
                if request.session.get('uid'):
                        return inicio(request)
                f = FormularioRegistro() # Creo un nuevo formulario...
                return render_to_response("registrarse.html", {'f': f}, # Y se lo paso a la plantilla.
					  context_instance=RequestContext(request))

        elif request.method == "POST": # Se va a registrar
                f = FormularioRegistro(request.POST)
                if f.is_valid():
                        try:
                                u = User.objects.get(username=f.cleaned_data['username']) # Me traigo los datos con f.cleaned_data
                                return render_to_response("registrarse.html", {'direccion':dir, 'msg': "Nombre de usuario ya existente!",'f' : f},
							  context_instance=RequestContext(request))
                        except User.DoesNotExist:
                                if f.cleaned_data['password'] != f.cleaned_data['confirm']:
                                        return render_to_response("registrarse.html",{'direccion':dir,'msg': "Contrase&ntilde;as no coinciden!",'f': f},
								  context_instance=RequestContext(request))
                                else:
                                        username=f.cleaned_data['username']
                                        u = User(username=username, email=f.cleaned_data['correo'],password=f.cleaned_data['password'])
                                        nombre = f.cleaned_data['nombre']
                                        apellido = f.cleaned_data['apellido']
                                        u.first_name=nombre
                                        u.last_name=apellido
                                        u.is_staff=False
                                        u.is_active=True
                                        u.is_superuser=False
                                        u.save()
                                        return render_to_response("login.html", {'msg' : "Usuario ya creado!!"},
								  context_instance=RequestContext(request))
                else:
                        return render_to_response("registrarse.html",{ 'msg': "Uno de sus datos no tiene el formato adecuado",'f': FormularioRegistro()})



def modificar_user(request):
        dir = "http://127.0.0.1:8000/template/bugtracker/"

        if request.method == "GET":
                f = FormularioModificarUser()
                return render_to_response("modificar_user.html", {'direccion':dir,'msg': "", 'f': f},
					  context_instance=RequestContext(request))

        elif request.method == "POST":
                f = FormularioModificarUser(request.POST)
                if f.is_valid():
                        uid=request.session.get('uid')
                        u=User.objects.get(id=uid)
                        nombre=f.cleaned_data['nombre']
                        apellido=f.cleaned_data['apellido']
                        password=f.cleaned_data['password']
                        confirm=f.cleaned_data['confirm']
                        correo=f.cleaned_data['correo']
                        if nombre!="":
                                u.first_name=nombre
                        if apellido!="":
                                u.last_name=apellido
                        if correo!="":
                                u.email=correo
                        if password==confirm and password!="":
                                u.password=password

                        u.save()
                        return render_to_response("index.html", {'direccion':dir,'msg': "Usuario ya creado!!"},context_instance=RequestContext(request))

                else:
			return render_to_response("modificar_user.html", {'direccion':dir,'msg': "Error al modificar usuario", 'f': f},
						  context_instance=RequestContext(request))

def modificar_admin(request):
        dir = "http://127.0.0.1:8000/template/bugtracker/"

        if request.method == "GET":
                f =FormularioUsuarioAd()
                return render_to_response("bugtracker/registrar_error.html", {'direccion':dir,'msg': "", 'f': f},
					  context_instance=RequestContext(request))

        elif request.method == "POST":
                f = FormularioUsuarioAd(request.POST)

                if f.is_valid():
                        return render_to_response("bugtracker/index.html", {'direccion':dir,'msg': "Aplicacion ya creado!!"},context_instance=RequestContext(request))

                else:
                        return render_to_response("bugtracker/modificar_admin.html", {'direccion':dir,'msg': "Error al modificar usuario", 'f': f},
						  context_instance=RequestContext(request))


def eliminar_usuario(request,user_iden):
        u=User.objects.get(pk=user_iden)
        u.delete()
        return render_to_response("listar_user.html", {'direccion':dir,'msg': "Usuario ya creado!!"},context_instance=RequestContext(request))

