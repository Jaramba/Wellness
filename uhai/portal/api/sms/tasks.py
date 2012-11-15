from urllib import urlopen, urlencode
import requests, sys

from django.db import transaction
from celery.task import periodic_task

from messaging import SMSProcessor
from datetime import timedelta

@periodic_task(run_every=timedelta(seconds=1))
def outgoingmessage_pt():
	SMSProcessor().process_outgoingmessages()

@periodic_task(run_every=timedelta(seconds=1))
def incomingmessage_pt():
	SMSProcessor().process_incomingmessages()
	