from django.conf import settings
from django.http import HttpResponse

from models import SmsMessageOutbox
from tasks import africastalking as send_sms

from string import Template
from datetime import datetime

import logging

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)
 
@csrf_exempt
def new_message(request):
	if request.method == "GET" or request.method == "POST":
		logger.debug(request.REQUEST)
	return HttpResponse(REQUEST)
	