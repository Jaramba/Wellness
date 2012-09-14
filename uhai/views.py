from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response, redirect

from django.template.defaultfilters import slugify
from django.template.context import RequestContext

from uhai.userprofile.forms import RoleChooserForm
from uhai.programs.models import DiagnosisQuestionnaire


from datetime import datetime

@login_required
def dashboard(request, template_name='core/dashboard.html', data={}):
    if not request.session.get('use_page_as'):
        request.session['use_page_as'] = slugify(request.user.profile.main_role)
    if request.session.get('use_page_as') == 'patient':pass
    data['diagnosisquestionnaires'] = DiagnosisQuestionnaire.objects.all()
    return render_to_response(template_name, data, context_instance= RequestContext(request))

def index(request, template_name='index.html', data={}):
	if request.user.is_authenticated():
		return redirect('home')
	return render_to_response(template_name, data, context_instance= RequestContext(request))

@login_required
def use_as(request, type=None):
	if request.method == "POST":
		form = RoleChooserForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			profile = form.save()
			request.session['use_page_as'] = slugify(profile.main_role)
			return redirect('/')
	else:
		if type:
			request.session['use_page_as'] = type
		else:
			if not request.user.profile.main_role:
				data = {}
				template_name = 'use_as.html'	
				return render_to_response(template_name, data, context_instance=RequestContext(request))
	return redirect(request.META.get('HTTP_REFERER', '/'))
