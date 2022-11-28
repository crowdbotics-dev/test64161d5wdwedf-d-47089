"""
WSGI config for test64161d5wdwedf_d_47089 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test64161d5wdwedf_d_47089.settings')

application = get_wsgi_application()
