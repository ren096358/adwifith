"""
WSGI config for adwifith project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.insert(0, '/var/www/html/adwifith_test/adwifith')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adwifith.settings")

application = get_wsgi_application()
