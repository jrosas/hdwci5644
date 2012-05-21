from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template import Context, loader
from bugtracker.models import Error,ComenRep,Mensaje
from django.contrib.auth.models import User
from django.http import HttpResponse

def index(request):
	return HttpResponse("Estas en el indice")

def mensajes(request,bugtracker_id):
	return HttpResponse("Estas en el indice %s" % bugtracker_id)

def login(request, bugtracker_id):
	return HttpResponse("Este es: %s" % bugtracker_id)

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
    except Error.DoesNotExist:
        # Redisplay the poll voting form.
        return Http404
    else:
	return render_to_response('bugtracker/modificar.html', {'seleccionado':seleccionado}, context_instance=RequestContext(request))

def guardar(request, error_id):

    try:
	valor = Error.objects.get(pk=error_id)
    except Error.DoesNotExist:
        # Redisplay the poll voting form.
        return Http404
    else:
	return render_to_response('bugtracker/error.html', {'valor':valor}, context_instance=RequestContext(request))
	

