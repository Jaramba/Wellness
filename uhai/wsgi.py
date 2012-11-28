import os
from django.utils.importlib import import_module

os.environ['DJANGO_SETTINGS_MODULE'] = settings_module = 'uhai.config.environment.%s' % os.environ.get('STAGE', 'production')

from django.core import management

management.setup_environ(import_module(settings_module))  # mimic manage.py

utility = management.ManagementUtility()
command = utility.fetch_command('runserver')
command.validate()  # validate the models - *THIS* is what was missing

import djcelery
djcelery.setup_loader()

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()