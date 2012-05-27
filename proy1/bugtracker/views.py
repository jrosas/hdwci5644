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

def inicio(request):
		return render_to_response("bugtracker/inicio.html")


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
	

