# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required
from wellness.core.views import model_view
from django.shortcuts import get_object_or_404

encounter = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
order = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
visit = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
immunization = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
trackingfield = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
trackingrecord = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
patienttrackingrecord = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))

@login_required
def problem(request, problem_type='', *args, **kwargs):
    get_object_or_404(ProblemType,slug=problem_type)
    return model_view(request, *args, **kwargs)
