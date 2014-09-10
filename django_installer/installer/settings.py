from os.path import dirname, join, realpath

from django.utils.crypto import get_random_string

_PROJECT_ROOT = realpath(dirname(__file__))


# TODO: fix this by extracting the hostname portion from our command line
DEBUG = True  # so we don't have to set ALLOWED_HOSTS m(

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'django_installer.installer.urls'

# taken from django/core/management/commands/startproject.py
__SECRET_KEY_CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = get_random_string(50, __SECRET_KEY_CHARS)

TEMPLATE_DIRS = (join(_PROJECT_ROOT, "templates"),)
