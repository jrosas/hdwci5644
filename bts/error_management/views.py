# Create your views here.
from django.shortcuts import render_to_response
from error_management.models import Error
from django.template import RequestContext
from forms import FormularioModificarError, FormularioRegistrarError
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import redirect

def registrar_error(request):
        dir = "http://127.0.0.1:8000/template/bugtracker/"
	session=Session.objects.get(session_key=request.session.session_key)
	uid=session.get_decoded().get('_auth_user_id')
        u=User.objects.get(pk=uid)

	if u.has_perm('error_management.add_error'):
		if request.method == "GET":
        		f = FormularioRegistrarError()
        		return render_to_response("registrar_error.html", {'direccion':dir,'msg': "", 'f': f}, 
                        	          context_instance=RequestContext(request))
    	
		elif request.method == "POST":
       			f=FormularioRegistrarError(request.POST)
			if f.is_valid():
				estado=f.cleaned_data['estado']
				prioridad=f.cleaned_data['prioridad']
				original=f.cleaned_data['original']
				informacion_duplicacion=f.cleaned_data['informacion_duplicacion']
				aplicacion=f.cleaned_data['aplicacion']
				usuario_reporto=u;
				usuario_encargado=u;
               			e = Error(estado=estado,prioridad=prioridad,original=original,informacion_duplicacion=informacion_duplicacion,usuario_reporto=usuario_reporto,usuario_encargado=usuario_encargado, aplicacion=aplicacion)
				e.save()
                  		return render_to_response("error_list.html", {'direccion':dir,'msg': "Error ya creado!!"},context_instance=RequestContext(request))

			else:
	        		return render_to_response("registrar_error.html", {'direccion':dir,'msg': "Error al modificar usuario", 'f': f}, 
                        	          context_instance=RequestContext(request))
	else:
      		return render_to_response("index.html", {'direccion':dir,'msg': "No tiene permisos"}, 
                                	  context_instance=RequestContext(request))




def modificar_error(request,error_iden):
        dir = "http://127.0.0.1:8000/template/bugtracker/"

	session=Session.objects.get(session_key=request.session.session_key)
	uid=session.get_decoded().get('_auth_user_id')
        u=User.objects.get(pk=uid)

	if u.has_perm('error_management.change_error'):
		if request.method == "GET":
        		f = FormularioModificarError()
        		return render_to_response("modificar_error.html", {'error_iden':error_iden,'direccion':dir,'msg': "", 'f': f}, 
                        	          context_instance=RequestContext(request))

    		elif request.method == "POST":
        		f = FormularioModificarError(request.POST)
       			if f.is_valid():
               			e = Error.objects.get(id=error_iden)
				estado=f.cleaned_data['estado']
				if estado!="":
					e.estado=estado
				e.save()
                        	return redirect('/errores')
                  		#return render_to_response("error_list.html", {'direccion':dir,'msg': "Usuario ya creado!!"},context_instance=RequestContext(request))

			else:
	        		return render_to_response("modificar_error.html", {'direccion':dir,'msg': "Error al modificar usuario", 'f': f}, 
                                	  context_instance=RequestContext(request))
	else:
		
	        		return render_to_response("index.html", {'direccion':dir,'msg': "No tiene permisos"}, 
                                	  context_instance=RequestContext(request))


def mostrar_comentarios(request,error_iden):
	e = Error.objects.get(id=error_iden)
	return render_to_response("comentar_error.html", {'direccion':dir,'msg': "Usuario ya creado!!",'error':e},context_instance=RequestContext(request))


def eliminar_error(request,error_iden):
        e=Error.objects.get(id=error_iden)
        e.delete()
        return render_to_response("listar_error.html", {'direccion':dir,'msg': "Usuario ya creado!!"},context_instance=RequestContext(request))
