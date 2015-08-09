from .base import *
import os


ADMINS = (
    ('Zachery Tapp', 'zacherytapp@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'weddinglocal',
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT',''),
    }
}


# You might want to use sqlite3 for testing in local as it's much faster.
if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/weddingapp_test.db',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
