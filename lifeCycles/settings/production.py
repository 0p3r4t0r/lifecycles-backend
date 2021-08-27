import os
from .base import *

ALLOWED_HOSTS = ['localhost']

# Security
# https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# https://docs.djangoproject.com/en/3.2/ref/settings/
SECURE_SSL_REDIRECT = True


# Database
DATABASES = {
    'default': {
        'ENGINE': os.environ['DEFAULT_SQL_ENGINE'],
        'NAME': os.environ['DEFAULT_SQL_DATABASE'],
        'USER': os.environ['DEFAULT_SQL_USER'],
        'PASSWORD': os.environ['DEFAULT_SQL_PASSWORD'],
        'HOST': os.environ['DEFAULT_SQL_HOST'],
        'PORT': os.environ['DEFAULT_SQL_PORT'],
    }
}
