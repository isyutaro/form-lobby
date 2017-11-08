"""
WSGI config for form_lobby project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/

"""

import os

from django.core.wsgi import get_wsgi_application

environment = os.environ.get('PROJECT_ENV', 'development')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "form_lobby.settings.%s" % environment)

application = get_wsgi_application()
