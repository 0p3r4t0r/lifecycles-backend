import os
from .base import *

# Security
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}