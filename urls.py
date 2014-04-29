# - * - mode: python; coding: utf-8 - * 
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r"^$", direct_to_template, {"template": "index.html"}),
	url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
