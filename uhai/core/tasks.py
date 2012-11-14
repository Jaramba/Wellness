import redis
import requests

from celery.task import task

from django.conf import settings
from django.db import transaction
from django.utils.timezone import now

