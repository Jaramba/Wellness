from django.http import HttpResponse
from tasks import process_outgoingmessages

import logging

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)

@login_required
def new_message(request):
    if request.method == "GET" or request.method == "POST":
        process_outgoingmessages.delay(request.user.pk, 'We will Kill Nes')
    return HttpResponse(request.GET)
    
@login_required
def out_message(request):
    if request.method == "GET" or request.method == "POST":
        publish('We will not Kill Nes', request.user.pk)
    return HttpResponse('<b>Sent</b> Mail')
    
