from django.conf import settings
import sys
import os
from os.path import join, abspath, dirname

# PATH vars
here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

sys.path.insert(0, root('apps'))

# SECURITY WARNING: keep the secret key a secret!
SECRET_KEY = os.environ.get('SECRET_KEY','')

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
    'ckeditor',
)

PROJECT_APPS = (
    'home',
    'story',
    'gallery',
    'core',
    'party',
    'information',
    'travel',
    'registry'

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

# CKEditor Settings
# More information found here:
# https://github.com/django-ckeditor/django-ckeditor
CKEDITOR_UPLOAD_PATH = root('assets', 'uploads')
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Advanced',
    },
    'default': {
        'toolbar': 'Advanced',
        'height': 300,
        'width': 700,
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# --------------------------------------------------------------------
# Support for AWS (How I figured it out):
# https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/
# http://blog.doismellburning.co.uk/2012/07/14/using-amazon-s3-to-host-your-django-static-files/
AWS_STORAGE_BUCKET_NAME = 'zakk-and-kira-wedding'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID','')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY','')

# Custom app domain for my stuff on Amazon S3
AWS_S3_CUSTOM_DOMAIN = '%s' % 's3-us-west-2.amazonaws.com/zakk-and-kira-wedding'

# Tell the staticfiles app to use S3Boto storage (when running `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Points to S3 folders - see Django docs above.
STATIC_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN
STATIC_ROOT = root('static')

MEDIAFILES_LOCATION = 'uploads'
MEDIA_ROOT = root('assets', 'uploads')
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

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
if PRODUCTION_INSTANCE == 'True':
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
