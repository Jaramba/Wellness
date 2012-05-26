import os
import sys

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'wellness.conf.settings'

from wellness.conf import settings

import django.core.management
django.core.management.setup_environ(settings)  # mimic manage.py
utility = django.core.management.ManagementUtility()
command = utility.fetch_command('runserver')
command.validate()  # validate the models - *THIS* is what was missing

application = WSGIHandler()