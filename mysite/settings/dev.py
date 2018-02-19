from __future__ import absolute_import, unicode_literals

from .base import *

try:
    from .local import *
except ImportError:
    pass

INSTALLED_APPS.extend([
    'debug_toolbar',
])

MIDDLEWARE.extend([
    'debug_toolbar.middleware.DebugToolbarMiddleware',
])

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7e^+l4gx9_avmjaqm9ep46w!df-+(9j(l+bm&h=qt%p!yi&9pt'

INTERNAL_IPS = ['127.0.0.1', 'localhost']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
