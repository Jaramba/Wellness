from django.conf import settings
from django.http import HttpResponse

from models import SmsMessageOutbox
from africatalking import send as send_sms

from string import Template
from datetime import datetime

import logging

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)

@login_required
def send(request):
    responses = []
    messages = SmsMessageOutbox.objects.filter(timestamp__isnull=True)
    for message in messages:
        response = send_sms(message.destination, message.text)
        responses.append(response)
        message.gateway_response = response
        message.timestamp = datetime.now()
        message.save()
    return HttpResponse('Messages sent:<br />' + '<br />'.join(responses))
 
@csrf_exempt
def new_message(request):
	if request.method == "GET" or request.method == "POST":
		logger.debug(request.REQUEST)
	return HttpResponse(REQUEST)
	