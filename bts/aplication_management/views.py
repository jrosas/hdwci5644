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
from forms import FormularioCrearAplicacion
from aplication_management.models import Aplicacion


def all_aplication (request):
    list_aplication = []
    for app in Aplicacion.objects.all():
        app_item = {}
        app_item['aplication_object']=app
        list_aplication.append(app_item)
    return render_to_response('app_list.html', { 'list_aplication': list_aplication })


def crear_aplicacion(request):
        dir = "http://127.0.0.1:8000/template/bugtracker/"

        if request.method == "GET":
                f = FormularioCrearAplicacion()
                return render_to_response("crear_aplicacion.html", {'direccion':dir,'msg': "", 'f': f},
                                  context_instance=RequestContext(request))

        elif request.method == "POST":
                f=FormularioCrearAplicacion(request.POST)
                if f.is_valid():
                        nombre=f.cleaned_data['nombre']
                        version=f.cleaned_data['version']
                        a = Aplicacion(nombre=nombre,version=version)
                        a.save()
                        return render_to_response("index.html", {'direccion':dir,'msg': "Aplicacion ya creado!!"},context_instance=RequestContext(request))

                else:
                        return render_to_response("crear_aplicacion.html", {'direccion':dir,'msg': "Error al modificar usuario", 'f': f},
                                  context_instance=RequestContext(request))


def eliminar_aplicacion(request,aplicacion_iden):
	a=Aplicacion.objects.get(id=aplicacion_iden)
	a.delete()
	return render_to_response("listar_aplicaciones.html", {'direccion':dir,'msg': "Usuario ya creado!!"},context_instance=RequestContext(request))
