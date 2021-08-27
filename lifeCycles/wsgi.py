"""
WSGI config for lifeCycles project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

from .settings.env import set_django_settings_module
from django.core.wsgi import get_wsgi_application

set_django_settings_module()

application = get_wsgi_application()
