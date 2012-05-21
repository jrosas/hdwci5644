from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bts.views.home', name='home'),
    # url(r'^bts/', include('bts.foo.urls')),

    url(r'^bugtracker/$', 'bugtracker.views.index'),
    url(r'^bugtracker/error/$', 'bugtracker.views.error'),
    url(r'^bugtracker/error/modificar/$','bugtracker.views.modificar'),
    url(r'^bugtracker/error/modificar/guardar/(?P<error_id>\d+)/$','bugtracker.views.guardar'),
    url(r'^bugtracker/(?P<bugtracker_id>\d+)/$', 'bugtracker.views.login'),
    url(r'^bugtracker/(?P<bugtracker_id>\d+)/$', 'bugtracker.views.mensajes'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
