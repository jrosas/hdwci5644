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
from message_management.models import Mensaje
from django.contrib.auth.models import User, Group, Permission
from django.http import HttpResponse
from django.conf import settings
from forms import FormularioEnviarMensaje


def enviar_mensaje(request):
        dir = "http://127.0.0.1:8000/template/bugtracker/"

        if request.method == "GET":
                f = FormularioEnviarMensaje()
                return render_to_response("enviar_mensaje.html", {'direccion':dir,'msg': "", 'f': f},
                                  context_instance=RequestContext(request))

        elif request.method == "POST":
                f = FormularioEnviarMensaje(request.POST)
                if f.is_valid():
                        emisor = f.cleaned_data['emisor']
                        receptor = f.cleaned_data['receptor']
                        asunto = f.cleaned_data['asunto']
                        contenido=f.cleaned_data['contenido']
                        m = Mensaje(emisor=emisor,receptor=receptor,asunto=asunto,contenido=contenido)
                        m.save()
                        return render_to_response("index.html", {'direccion':dir,'msg': "Usuario ya creado!!"},context_instance=RequestContext(request))

                else:
                        return render_to_response("enviar_mensaje.html", {'direccion':dir,'msg': "Error al modificar usuario", 'f': f},
                                  context_instance=RequestContext(request))


def eliminar_entrada(request,mensaje_iden):
        dir = "http://127.0.0.1:8000/template/bugtracker/"
        m = Mensaje.objects.get(id_m=mensaje_iden)
        m.delete()
        return render_to_response("listar_mensajes_entrada.html", {'direccion':dir,'msg': "Usuario ya creado!!"},context_instance=RequestContext(request))

def eliminar_salida(request,mensaje_iden):
        dir = "http://127.0.0.1:8000/template/bugtracker/"
        m = Mensaje.objects.get(id_m=mensaje_iden)
        m.delete()
        return render_to_response("listar_mensajes_salida.html", {'direccion':dir,'msg': "Usuario ya creado!!"},context_instance=RequestContext(request))


def bandeja_entrada(request):
        dir = "http://127.0.0.1:8000/template/bugtracker/"
        session=Session.objects.get(session_key=request.session.session_key)
        uid=session.get_decoded().get('_auth_user_id')
        u=User.objects.get(pk=uid)

	m = Mensaje.objects.filter(receptor=u)
        return render_to_response("listar_mensajes_entrada.html", {'direccion':dir,'bandeja':m,'msg': "Usuario ya creado!!"},context_instance=RequestContext(request))


def bandeja_salida(request):
        dir = "http://127.0.0.1:8000/template/bugtracker/"
        session=Session.objects.get(session_key=request.session.session_key)
        uid=session.get_decoded().get('_auth_user_id')
        u=User.objects.get(pk=uid)

	m = Mensaje.objects.filter(emisor=u)
        return render_to_response("listar_mensajes_salida.html", {'direccion':dir,'bandeja':m,'msg': "Usuario ya creado!!"},context_instance=RequestContext(request))


