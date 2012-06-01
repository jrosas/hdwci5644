from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import DetailView, ListView
from error_management.models import Error
from aplication_management.models import Aplicacion
from message_management.models import Mensaje
from django.contrib.auth.models import User

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bts.views.home', name='home'),
    # url(r'^bts/', include('bts.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aplicaciones/$',  ListView.as_view(model=Aplicacion,
                                        template_name='aplicacion_list.html')),
    url(r'^errores/$', ListView.as_view(model=Error,
                                        template_name='error_list.html')),
    url(r'^mensajes/$', ListView.as_view(model=Mensaje,
                                        template_name='mensaje_list.html')),
    url(r'^usuarios/$', ListView.as_view(model=User,
                                    template_name='user_list.html')),
    url(r'^usuarios/registrarse$', 'user_management.views.registrarse'),
    url(r'^usuarios/iniciada/$', 'views.index'),
    url(r'^usuarios/pre_login$', 'user_management.views.pre_login'),
    url(r'^usuarios/login$', 'user_management.views.logins'),
    url(r'^usuarios/logout$', 'user_management.views.logouts'),
    url(r'^usuarios/modificar_user$', 'user_management.views.modificar_user'),
    url(r'^usuarios/modificar_admin$', 'user_management.views.modificar_admin'),

    url(r'^errores/error/(?P<pk>\d+)$', DetailView.as_view(model=Error,
                                    template_name='error_detail.html')),
    url(r'^errores/editar/(?P<error_iden>\d+)$', 'error_management.views.modificar_error'),
    url(r'^errores/comentar/(?P<error_iden>\d+)$', 'error_management.views.mostrar_comentarios'),
    url(r'^errores/add/$', 'error_management.views.registrar_error'),
    url(r'^$','views.index'),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),   
    (r'^comments/', include('django.contrib.comments.urls')),


)
