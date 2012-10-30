# Create your views here.
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.http import Http404, HttpResponse

from forms import *
from models import *
from uhai.portal.my.patients.models import Patient

from uhai.core.views import *

@login_required
def index(request, problem_type='', template_name = "records/index.html", *args, **kwargs):
    data = {}
    return render_to_response(template_name, data, context_instance= RequestContext(request))

@login_required
def encounter(request, user_pk=None, encounter_type=None, extra_data={}, queryset=None, *args, **kwargs):
    kwargs['queryset'] = queryset.filter(type__slug=encounter_type) if encounter_type else queryset

    def save_form(form, commit=False):
        obj = form.save(commit=commit)
        obj.user = request.user
        obj.end_time = obj.follow_up_date = obj.start_time
        obj.text = 'Vacination for %s' % obj.user
        obj.save()
        return obj
    kwargs['save_form'] = save_form
    extra_data['encounter_type'] = encounter_type

    return user_model_view(request, extra_data=extra_data, *args, **kwargs)

@login_required
def diagnosis(request, queryset=None, problem_type='', extra_data={}, *args, **kwargs):
	if problem_type:
		extra_data['problem_type'] = get_object_or_404(ProblemType, slug=problem_type)
	
	kwargs['queryset'] = queryset.filter(problem__type__slug=problem_type) if problem_type else queryset        
	return role_model_view(request, extra_data=extra_data, *args, **kwargs)
	