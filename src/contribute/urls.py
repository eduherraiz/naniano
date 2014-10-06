#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

from .views import QuickEntry


urlpatterns = (

    url(r'contribute/$', QuickEntry.as_view(), name='contribute'),

)