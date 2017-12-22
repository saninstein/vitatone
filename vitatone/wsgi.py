"""
WSGI config for vitatone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vitatone.settings")


application = get_wsgi_application()
if 'HEROKU_PROD' in os.environ:
    application = DjangoWhiteNoise(application)
