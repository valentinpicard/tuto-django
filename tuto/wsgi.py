"""
WSGI config for tuto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

"""
WSGI - Web Server Gateway Interface
It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tuto.settings') # Used to locate the settings module

application = get_wsgi_application()
