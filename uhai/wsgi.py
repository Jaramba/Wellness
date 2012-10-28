import os

STAGE = os.environ.get('STAGE', 'staging')
os.environ['DJANGO_SETTINGS_MODULE'] = 'uhai.conf.environment.%s' % STAGE

import sys

from django.core import management
from django.conf import settings

management.setup_environ(settings)  # mimic manage.py

utility = management.ManagementUtility()
command = utility.fetch_command('runserver')
command.validate()  # validate the models - *THIS* is what was missing

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()