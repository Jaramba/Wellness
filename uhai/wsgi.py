import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'uhai.conf.settings'

import sys

from django.core import management
from uhai.conf import settings

management.setup_environ(settings)  # mimic manage.py

utility = management.ManagementUtility()
command = utility.fetch_command('runserver')
command.validate()  # validate the models - *THIS* is what was missing

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()