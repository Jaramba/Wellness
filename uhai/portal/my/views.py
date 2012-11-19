from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect

from django.template.defaultfilters import slugify
from django.template.context import RequestContext

from uhai.portal.my.programs.models import DiagnosisQuestionnaire

def switchboard(request, template_name='portal/my/switchboard.html', data={}):
	raise Exception(request.user)
	return render_to_response(template_name, data, context_instance= RequestContext(request))