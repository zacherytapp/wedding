"""
WSGI config for weddingapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import os
from os.path import abspath, dirname
from sys import path

SITE_ROOT = dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)


os.environ.get("DJANGO_SETTINGS_MODULE", "weddingapp.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
