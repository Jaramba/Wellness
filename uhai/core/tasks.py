import redis
import requests

from celery.task import task

from django.conf import settings
from django.db import transaction
from django.utils.timezone import now

@task
reminders

#Create a task to create reminders to:
	# -Patients who have prescriptions
	# -Patients who are enrolled to programs; check on progress vis-a-vis 
	# -Patients who have not filled in the latest vitals, once a week? 
#create a task to check on program progress...
#Create a task to send out Emails
#create a task to rebuild indexes for search
#Create a task to send sms; Use Pub/Sub instead of saving the messages in the DB... 