from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.shortcuts import render_to_response

def index(request, template_name = ""):
	if request.user.is_authenticated():
		template_name = 'core/dashboard.html'
	else:
		template_name = 'index.html'
	data = {}
	return render_to_response(template_name, data, context_instance= RequestContext(request))

@login_required
def use_as(request, type):
	request.session['use_page_as'] = type
	return HttpResponseRedirect('/')
