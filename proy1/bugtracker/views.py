from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template import Context, loader
from bugtracker.models import Error,ComenRep,Mensaje
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings
from bugtracker.forms import FormularioRegistro, FormularioModificarUser

def inicio(request):
		return render_to_response("bugtracker/inicio.html")


def index(request):
	uid = request.session.get('uid')
	t   = loader.get_template("bugtracker/index.html")
	try:
		u   = User.objects.get(id=uid)
		return render_to_response("bugtracker/index.html", {'user': u})
	except User.DoesNotExist:
		return HttpResponse(t.render(Context({})))
		

def pre_login(request):
	dir = "http://127.0.0.1:8000/template/bugtracker/"
	if request.session.get('uid'):
		return index(request)
	return render_to_response("bugtracker/login.html",{'msg': "", 'direccion':dir}, context_instance=RequestContext(request))


def logins(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request,user)
			return redirect('iniciada/')
            # Redirect to a success page.
		else:
			return HttpResponse("Su cuenta esta inactiva.")

            # Return a 'disabled account' error message
	else:
		return HttpResponse("Datos invalidos.")

	# Return an 'invalid login' error message.



def registrarse(request):
        dir = "http://127.0.0.1:8000/template/bugtracker/"
	if request.method == "GET": # Metodo GET, se va a registrar.
        	if request.session.get('uid'):
            		return inicio(request)
        	f = FormularioRegistro() # Creo un nuevo formulario...
        	return render_to_response("bugtracker/registrarse.html", {'direccion':dir,'msg': "", 'f': f}, # Y se lo paso a la plantilla.
                                  context_instance=RequestContext(request))
        
    	elif request.method == "POST": # Se va a registrar
        	f = FormularioRegistro(request.POST)
       		if f.is_valid():
            		try:
                		u = User.objects.get(username=f.cleaned_data['username']) # Me traigo los datos con f.cleaned_data
                		return render_to_response("bugtracker/registrarse.html", {'direccion':dir, 'msg': "Nombre de usuario ya existente!",'f' : f}, 
                                          context_instance=RequestContext(request))
            		except User.DoesNotExist:
                		if f.cleaned_data['password'] != f.cleaned_data['confirm']:
                    			return render_to_response("bugtracker/registrarse.html",{'direccion':dir,'msg': "Contrase&ntilde;as no coinciden!",'f': f}, 
                                              context_instance=RequestContext(request))
                		else:
                    			u = User(username=f.cleaned_data['username'], email=f.cleaned_data['correo'],password=f.cleaned_data['password'])
                        		nombre = f.cleaned_data['nombre']
                        		apellido = f.cleaned_data['apellido']
                        		u.first_name=nombre
                        		u.last_name=apellido
                        		u.is_staff=False
                        		u.is_active=True
                        		u.is_superuser=False

                    			u.save()
                    			return render_to_response("bugtracker/login.html", {'direccion':dir,'msg': "Usuario ya creado!!"}, 
                                              context_instance=RequestContext(request))
        	else:
            		return render_to_response("bugtracker/registrarse.html",{'direccion':dir, 'msg': "Uno de sus datos no tiene el formato adecuado.",'f': FormularioRegistro()})
        

def modificar_user(request):
        dir = "http://127.0.0.1:8000/template/bugtracker/"

	if request.method == "GET":
        	f = FormularioModificarUser()
        	return render_to_response("bugtracker/modificar_user.html", {'direccion':dir,'msg': "", 'f': f}, 
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
                  	return render_to_response("bugtracker/index.html", {'direccion':dir,'msg': "Usuario ya creado!!"},context_instance=RequestContext(request))
		
		else:
	        	return render_to_response("bugtracker/modificar_user.html", {'direccion':dir,'msg': "Error al modificar usuario", 'f': f}, 
                                  context_instance=RequestContext(request))
	


def mensajes(request):
	return HttpResponse("Estas en el indice")


def error(request):
	lastest_bugtracker_list_error=Error.objects.all().order_by('-id')[:10]
	c = Context({
	'lastest_bugtracker_list_error': lastest_bugtracker_list_error,
	})
	return render_to_response('bugtracker/error.html', {'lastest_bugtracker_list_error':lastest_bugtracker_list_error}, context_instance=RequestContext(request))

# ...

def modificar(request):
	try:
		seleccionado = Error.objects.get(pk=request.POST['id'])
	except User.DoesNotExist:
        # Redisplay the poll voting form.
		return Http404
	else:
		return render_to_response('bugtracker/modificar.html', {'seleccionado':seleccionado}, context_instance=RequestContext(request))

#def guardar(request, user_id):

 #   try:
#	valor = User.objects.get(pk=user_id)
 #   except User.DoesNotExist:
        # Redisplay the poll voting form.
 #       return Http404
  #  else:
#	return render_to_response('bugtracker/user.html', {'valor':valor}, context_instance=RequestContext(request))
	

