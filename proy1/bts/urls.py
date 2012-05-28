from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bts.views.home', name='home'),
    # url(r'^bts/', include('bts.foo.urls')),

    url(r'^bugtracker/$', 'bugtracker.views.inicio'),
    url(r'^bugtracker/error/$','bugtracker.views.error'),
    url(r'^bugtracker/pre_login/$', 'bugtracker.views.pre_login'),
    url(r'^bugtracker/login/$', 'bugtracker.views.logins'),
    url(r'^bugtracker/login/iniciada/$', 'bugtracker.views.inicio'),
    url(r'^bugtracker/registrarse/$', 'bugtracker.views.registrarse'),
    url(r'^bugtracker/modificar_user/$', 'bugtracker.views.modificar_user'),
    url(r'^bugtracker/modificar_error/(?P<error_iden>\d+)/$', 'bugtracker.views.modificar_error'),
    url(r'^bugtracker/modificar_admin/$', 'bugtracker.views.modificar_admin'),
    url(r'^bugtracker/registrar_error/$', 'bugtracker.views.registrar_error'),
    url(r'^bugtracker/crear_aplicacion/$', 'bugtracker.views.crear_aplicacion'),

#    url(r'^bugtracker/user/modificar/guardar/(?P<error_id>\d+)/$','bugtracker.views.guardar'),
#    url(r'^bugtracker/(?P<bugtracker_id>\d+)/$', 'bugtracker.views.login'),
    url(r'^bugtracker/(?P<bugtracker_id>\d+)/$', 'bugtracker.views.mensajes'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^template/bugtracker/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
