#!/usr/bin/env python
import os
import sys

STAGE = os.environ.get('STAGE', 'staging')
os.environ['DJANGO_SETTINGS_MODULE'] = 'uhai.conf.environment.%s' % STAGE

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.environ['DJANGO_SETTINGS_MODULE'])
	
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)