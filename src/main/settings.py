#!/usr/bin/env python
# encoding: utf-8
# --------------------------------------------------------------------------

import os
import sys

from configurations import Settings
from apconf.mixins import CachesMixin, DatabasesMixin, PathsMixin, LogsMixin
from apconf.mixins import SecurityMixin, DebugMixin, CompressMixin

from apconf import Options
opts = Options()

class Base(CachesMixin, DatabasesMixin, PathsMixin, LogsMixin, SecurityMixin,
           DebugMixin, CompressMixin, Settings):

    # --------------------------------------------------------------------------
    # Configuraciones imprescindibles
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    INSTALLED_APPS = (
        'admin_tools',
        'admin_tools.theming',
        'admin_tools.menu',
        'admin_tools.dashboard',
        'admin_tools_zinnia',
        'django.contrib.auth',
        'django.contrib.admin',
        'django.contrib.sites',
        'django.contrib.sessions',
        'django.contrib.contenttypes',
        'django.contrib.staticfiles',
        'django.contrib.messages',
        'django_extensions',
        'modeltranslation',
        'django_comments',
        'zinnia_bootstrap',
        'apconf',
        'south',
        'raven.contrib.django.raven_compat',
        "compressor",
        "django_mailer",
        "tagging",
        "mptt",
        "zinnia",
        # 'zinnia_wymeditor',
        'tinymce',
        # 'ckeditor',
        'django_extensions',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.debug',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'zinnia.context_processors.version',  # Optional
    )

    TEMPLATE_LOADERS = (
         'app_namespace.Loader',
         'django.template.loaders.filesystem.Loader',
         'django.template.loaders.app_directories.Loader',
     )


    ROOT_URLCONF = 'main.urls'

    WSGI_APPLICATION = 'main.wsgi.application'

    # Internacionalización
    LANGUAGE_CODE = 'es'

    gettext = lambda s: s
    LANGUAGES = (
        ('es', gettext('Spanish')),
    )

    TIME_ZONE = 'Europe/Madrid'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    APP_SLUG = opts.get('APP_SLUG', 'rajoy')

    # Para tests unitarios. Db en memoria
    if 'test' in sys.argv:
        SOUTH_TESTS_MIGRATE = False
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3'
            }
        }

    TEMPLATE_DIRS = ('templates', )

    # Sites...
    SITE_ID = 1

    # Configuración correo
    EMAIL_BACKEND = 'django_mailer.smtp_queue.EmailBackend'
    DEFAULT_FROM_EMAIL = opts.get('DEFAULT_FROM_EMAIL', 'demo@apsl.net')


    TINYMCE_DEFAULT_CONFIG = {
        'plugins': "table,spellchecker,paste,searchreplace",
        'theme': "advanced",
        'cleanup_on_startup': True,
        'custom_undo_redo_levels': 10,
    }
    TINYMCE_SPELLCHECKER = True
    TINYMCE_COMPRESSOR = True

    CKEDITOR_UPLOAD_PATH = "uploads/"
    CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'