from .base import *
import os


DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['127.0.0.1', '127.0.0.1']

ADMINS = (
    ('Zachery Tapp', 'zacherytapp@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'weddingdb',
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}
