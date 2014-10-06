#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from contribute.urls  import urlpatterns as urlpatternscontribute
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^', include('zinnia.urls', namespace='zinnia')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
)


urlpatterns += i18n_patterns(
    '',
)

urlpatterns += urlpatternscontribute

if settings.DEBUG:
    # Contenido estático
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )