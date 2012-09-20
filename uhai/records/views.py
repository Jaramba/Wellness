# Create your views here.
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.http import Http404, HttpResponse

from forms import *
from models import *
from uhai.patients.models import Patient

from uhai.core.views import *

@login_required
def index(request, problem_type='', template_name = "records/index.html", *args, **kwargs):
    data = {}
    return render_to_response(template_name, data, context_instance= RequestContext(request))

@login_required
def encounter(request, user_pk=None, encounter_type=None, queryset=None, *args, **kwargs):
    kwargs['queryset'] = queryset.filter(type__slug=encounter_type) if encounter_type else queryset

    def save_form(form, commit=False):
        obj = form.save(commit=commit)
        obj.user = request.user
        obj.end_time = obj.follow_up_date = obj.start_time
        obj.text = 'Vacination for %s' % obj.user
        obj.save()
        return obj
    kwargs['save_form'] = save_form
    kwargs['extra_context'] = kwargs.get('extra_context', {})
    kwargs['extra_context'].update(dict(encounter_type=encounter_type))

    return user_model_view(request, *args, **kwargs)

@login_required
def diagnosis(request, queryset=None, problem_type='', extra_data={}, *args, **kwargs):
	if problem_type:
		extra_data['problem_type'] = get_object_or_404(ProblemType, slug=problem_type)
	
	kwargs['queryset'] = queryset.filter(problem__type__slug=problem_type) if problem_type else queryset
	return role_model_view(request, extra_data=extra_data, *args, **kwargs)
	
def report(request, template_name='userprofile/login.html', filename='report'):
    try:
		import pdfcrowd
		# create an API client instance
		client = pdfcrowd.Client("kanarelo", "05d18f129c5b5176f443a1eaa6f2e482")
		data = {}

		# convert a web page and store the generated PDF to a variable
		pdf = client.convertHtml(render_to_string(template_name, data, context_instance=RequestContext(request)))

		 # set HTTP response headers
		response = HttpResponse(mimetype="application/pdf")
		response["Cache-Control"] = "no-cache"
		response["Accept-Ranges"] = "none"
		response["Content-Disposition"] = "attachment; filename=%s.pdf" % filename

		# send the generated PDF
		response.write(pdf)
    except pdfcrowd.Error, why:
        response = HttpResponse(mimetype="text/plain")
        response.write(why)
    return response
