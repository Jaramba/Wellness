from django.http import HttpResponse

from models import SmsMessageOutbox
from messaging import SMSProcessor

import logging

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)

def new_message(request):
	if request.method == "GET" or request.method == "POST":
        SMSProcessor().publish('We will Kill Nes', request.user.pk, routing_key="incoming")
	return HttpResponse()
    
def out_message(request):
    if request.method == "GET" or request.method == "POST":
        SMSProcessor().publish('We will not Kill Nes', request.user.pk)
    return HttpResponse()
    
