"""
WSGI config for cars_and_trucks_pho_48647 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "cars_and_trucks_pho_48647.settings"
)

application = get_wsgi_application()
