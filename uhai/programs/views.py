# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required
from uhai.core.views import model_view

from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template.context import RequestContext

from django.http import Http404, HttpResponse

program = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
programtype = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
programworkflow = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
programworkflowstate = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
enrolledprogram = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))

@login_required
def index(request, problem_type='', template_name = "programs/index.html", *args, **kwargs):
    data = {}
    return render_to_response(template_name, data, context_instance= RequestContext(request))
