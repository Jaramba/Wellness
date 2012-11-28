from urllib import urlopen, urlencode
import requests, sys

from django.db import transaction

from celery.schedules import crontab  
from celery.decorators import periodic_task, task

from messaging import *
from datetime import timedelta

from django.contrib.auth.models import User
import requests, sys

API_KEY='d7334eba615b1f843511eeae3994e5d8917947fd50b16d84b2add0ed2bb102cd'
BASEURL='https://api.africastalking.com/version1/messaging/'

@task
def process_outgoingmessages(user_pk, message):
    requests.post(
        BASEURL,
        params={ 
            'username': 'mukewa',
            'to': User.objects.get(pk=user_pk).profile.mobile_phone,
            'message': message
        },
        headers={
            'accept': 'application/json', 
            'apikey':API_KEY
        },
        verify=False, 
        config={'verbose': sys.stderr}
    )

@task
def process_incomingmessages():
    """Process all currently gathered clicks by saving them to the
    database."""
    for message in consumer.iterqueue():
        print message.body.get('text')
        raise Exception("NES!")
        message.ack()

    consumer.close()
    connection.close()
