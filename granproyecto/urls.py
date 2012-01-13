from django.conf.urls.defaults import patterns, include, url
from django.views.generic.list import ListView
from funcionalidad.models import Servicio

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'granproyecto.funcionalidad.views.index', name='index'),
     url(r'^add/$', 'granproyecto.funcionalidad.views.add', name='add'),
     url(r'^add2/$', 'granproyecto.funcionalidad.views.add2', name='add'),
     url(r'^view/$', ListView.as_view(model=Servicio)),
    # url(r'^granproyecto/', include('granproyecto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
