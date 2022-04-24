"""
WSGI config for Donghakgaemi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/ubuntu/donghak_gaemi')
sys.path.append('/venv_3.8/lib/python3.8/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Donghakgaemi.settings.base')

application = get_wsgi_application()
