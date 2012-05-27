from bugtracker.models import Error
from django.contrib import admin

admin.site.register(Error)

from bugtracker.models import ComenRep
from django.contrib import admin

admin.site.register(ComenRep)

from bugtracker.models import Mensaje
from django.contrib import admin

admin.site.register(Mensaje)

from bugtracker.models import Aplicacion
from django.contrib import admin

admin.site.register(Aplicacion)

from bugtracker.models import Aplicacion_Usuario
from django.contrib import admin

admin.site.register(Aplicacion_Usuario)
