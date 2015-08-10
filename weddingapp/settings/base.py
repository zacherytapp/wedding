import sys
import os
from os.path import join, abspath, dirname

# PATH vars

here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

sys.path.insert(0, root('apps'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY','')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
)

PROJECT_APPS = (
    'home',
)

INSTALLED_APPS += PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'weddingapp.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'weddingapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'weddingapp',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'  # 'Europe/London'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
AWS_STORAGE_BUCKET_NAME = 'zakk-and-kira-wedding'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID','')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY','')

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s' % 's3-us-west-2.amazonaws.com/zakk-and-kira-wedding'

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
STATIC_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN

MEDIA_ROOT = root('assets', 'uploads')
MEDIA_URL = '/media/'

# Additional locations of static files
STATICFILES_DIRS = (
    root('assets'),
)

TEMPLATE_DIRS = (
    root('templates'),
)

# Checks to see if this is a production instance - if
# it is, it tells this document which sub-settings to pull from
PRODUCTION_INSTANCE = os.environ['PRODUCTION_INSTANCE']
if PRODUCTION_INSTANCE == True:
    try:
        from .production import *
    except ImportError:
        pass
else:
    try:
        from .local import *
    except ImportError:
        pass


# importing test settings file if necessary
if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    from .testing import *
