import os
from django.utils.importlib import import_module

STAGE = os.environ.get('STAGE', 'staging')
os.environ['DJANGO_SETTINGS_MODULE'] = settings_module = 'uhai.conf.environment.%s' % STAGE

from django.core import management

management.setup_environ(import_module(settings_module))  # mimic manage.py

utility = management.ManagementUtility()
command = utility.fetch_command('runserver')
command.validate()  # validate the models - *THIS* is what was missing

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()