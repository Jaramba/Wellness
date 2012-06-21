from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from django.shortcuts import render_to_response

@login_required
def calendar(request, template_name="reminders/calendar.html"):
	return render_to_response(template_name, {}, context_instance=RequestContext(request))