from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from django.shortcuts import render_to_response

from uhai.core.views import *
from models import *

from datetime import date, datetime, time, timedelta


@login_required
def reminders(request, template_name="reminders/reminders.html"):
	dates = []
	for n in range(0, 7):		
		day = date.today() + timedelta(days=n)
		dates += [[day, Event.objects.filter(user=request.user, start_time__day=day.day)]]
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))