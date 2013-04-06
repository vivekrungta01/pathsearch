from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import settings;

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pathsearch.views.home', name='home'),
    # url(r'^pathsearch/', include('pathsearch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', TemplateView.as_view(template_name="index.html")),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT }),
     url(r'^ajax-list/','search.views.ajax_list',name='ajax_list'),
)