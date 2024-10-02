"""
WSGI config for app_validez_expertos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_validez_expertos.settings')#esto es para que sepa que settings usar en produccion

application = get_wsgi_application()
