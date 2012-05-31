# Create your views here.
from django.shortcuts import render_to_response
from aplication_management.models import Aplicacion

def all_aplication (request):
    list_aplication = []
    for app in Aplicacion.objects.all():
        app_item = {}
        app_item['aplication_object']=app
        list_aplication.append(app_item)
    return render_to_response('app_list.html', { 'list_aplication': list_aplication })
