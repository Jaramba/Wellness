# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.http import Http404

from forms import *
from models import *
from uhai.patients.models import Patient

from uhai.core.views import model_view, role_model_view

#CRUD
order = login_required(lambda request, *args, **kwargs: role_model_view(request, *args, **kwargs))
visit = login_required(lambda request, *args, **kwargs: role_model_view(request, *args, **kwargs))
trackingfield = login_required(lambda request, *args, **kwargs: role_model_view(request, *args, **kwargs))
encountertestresult = login_required(lambda request, *args, **kwargs: role_model_view(request, *args, **kwargs))
encountertest = login_required(lambda request, *args, **kwargs: role_model_view(request, *args, **kwargs))
problemtest = login_required(lambda request, *args, **kwargs: role_model_view(request, *args, **kwargs))

@login_required
def index(request, problem_type='', template_name = "records/index.html", *args, **kwargs):
    data = {}
    return render_to_response(template_name, data, context_instance= RequestContext(request))

@login_required
def encounter(request, patient_pk=None, encounter_type=None, data={}, queryset=None, *args, **kwargs):
	queryset = queryset.filter(patient__pk=patient_pk) if patient_pk else queryset
	kwargs['queryset'] = queryset.filter(type__slug=encounter_type) if encounter_type else queryset

	if request.method == "POST":
		def save_form(form):
			encounter = form.save(commit=False)
			try:
				encounter.patient = request.user.profile.patient if not patient_pk else queryset.get(pk=patient_pk)
			except Patient.DoesNotExist:
				raise Http404
			encounter.save()
			return encounter

		data['save_form'] = save_form
	kwargs.update(data)
	return role_model_view(request, *args, **kwargs)

@login_required
def diagnosis(request, queryset=None, problem_type='', extra_data={}, *args, **kwargs):
	if problem_type:
		extra_data['problem_type'] = get_object_or_404(ProblemType, slug=problem_type)
	
	kwargs['queryset'] = queryset.filter(problem__type__slug=problem_type) if problem_type else queryset
	return role_model_view(request, extra_data=extra_data, *args, **kwargs)