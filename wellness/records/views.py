# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext

from forms import *
from models import *

from wellness.core.views import model_view

#CRUD
encounter = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
order = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
visit = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
immunization = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
trackingfield = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
encountertestresult = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
encountertest = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
diagnosis = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
problemtest = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))

@login_required
def index(request, problem_type='', template_name = "records/index.html", *args, **kwargs):
    data = {}
    return render_to_response(template_name, data, context_instance= RequestContext(request))
