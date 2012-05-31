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
    url(r'^errores/error/(?P<pk>\d+)$', DetailView.as_view(model=Error,
                                    template_name='error_detail.html')),
    url(r'^errores/editar/(?P<error_iden>\d+)$', 'error_management.views.modificar_error'),
    url(r'^$','views.index'),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),   
    (r'^comments/', include('django.contrib.comments.urls')),

)
