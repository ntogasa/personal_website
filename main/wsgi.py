"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Set 'main.settings.development' as default settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings.development')
# If in production mode, use production settings
if os.environ.get('PROD'):
    DJANGO_SETTINGS_MODULE = 'main.settings.production'

application = get_wsgi_application()
