from django.conf.urls import patterns, include, url
from django.views.generic import DetailView
from bugtracker.models import Error
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bts.views.home', name='home'),
    # url(r'^bts/', include('bts.foo.urls')),

    url(r'^bugtracker/$', 'bugtracker.views.inicio'),
    url(r'^bugtracker/listar_error/$','bugtracker.views.listar_error'),
    url(r'^bugtracker/pre_login/$', 'bugtracker.views.pre_login'),
    url(r'^bugtracker/login/$', 'bugtracker.views.logins'),
    url(r'^bugtracker/login/iniciada/$', 'bugtracker.views.inicio'),
    url(r'^bugtracker/registrarse/$', 'bugtracker.views.registrarse'),
    url(r'^bugtracker/modificar_user/$', 'bugtracker.views.modificar_user'),
    url(r'^bugtracker/pre_modificar_error/modificar_error/(?P<error_iden>\d+)/$', 'bugtracker.views.modificar_error'),
    url(r'^bugtracker/pre_modificar_error/modificar_error/(?P<error_iden>\d+)/$', 'bugtracker.views.modificar_error'),
    url(r'^bugtracker/eliminar_mensaje/(?P<mensaje_iden>\d+)/$', 'bugtracker.views.eliminar_mensaje'),
    url(r'^bugtracker/pre_modificar_error/$', 'bugtracker.views.pre_modificar_error'),
    url(r'^bugtracker/modificar_admin/$', 'bugtracker.views.modificar_admin'),
    url(r'^bugtracker/enviar_mensaje/$', 'bugtracker.views.enviar_mensaje'),
    url(r'^bugtracker/registrar_error/$', 'bugtracker.views.registrar_error'),
    url(r'^bugtracker/crear_aplicacion/$', 'bugtracker.views.crear_aplicacion'),
    url(r'^bugtracker/mostrar_comentarios/(?P<error_iden>\d+)/$', 'bugtracker.views.mostrar_comentarios'),
    url(r'^bugtracker/listar_com_error/(?P<error_iden>\d+)/$', 'bugtracker.views.listar_com_error'),
#    url(r'^bugtracker/ver_error/(?P<pk>\d+)/$', DetailView.as_view(model=Error,template_name='bugtracker/ver_error.html')),
    (r'^comments', include('django.contrib.comments.urls')),
#    url(r'^bugtracker/user/modificar/guardar/(?P<error_id>\d+)/$','bugtracker.views.guardar'),
#    url(r'^bugtracker/(?P<bugtracker_id>\d+)/$', 'bugtracker.views.login'),
    url(r'^bugtracker/(?P<bugtracker_id>\d+)/$', 'bugtracker.views.mensajes'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^template/bugtracker/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
