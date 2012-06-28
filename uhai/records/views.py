# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from django.http import Http404

from forms import *
from models import *
from uhai.patient.models import Patient

from uhai.core.views import model_view

#CRUD
order = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
visit = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
immunization = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
trackingfield = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
encountertestresult = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
encountertest = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
problemtest = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))

@login_required
def index(request, problem_type='', template_name = "records/index.html", *args, **kwargs):
    data = {}
    return render_to_response(template_name, data, context_instance= RequestContext(request))

@login_required
def encounter(request, patient_number=None, encounter_type=None, data={}, queryset=None, *args, **kwargs):
	queryset = queryset.filter(patient__patient_number=patient_number) if patient_number else queryset
	kwargs['queryset'] = queryset.filter(type__slug=encounter_type) if encounter_type else queryset

	if request.method == "POST":
		def save_form(form):
			encounter = form.save(commit=False)
			try:
				encounter.patient = request.user.profile.patient if not patient_number else queryset.get(patient_number=patient_number)
			except Patient.DoesNotExist:
				raise Http404
			encounter.save()
			return encounter

		data['save_form'] = save_form
	kwargs.update(data)
	return model_view(request, *args, **kwargs)

@login_required
def diagnosis(request, queryset=None, problem_type='', *args, **kwargs):
	kwargs['queryset'] = queryset.filter(problem__type__slug=problem_type) if problem_type else queryset
	return model_view(request, *args, **kwargs)
