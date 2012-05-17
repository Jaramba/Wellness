# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required
from core.views import model_view

program = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
programtype = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
programworkflow = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
programworkflowstate = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
enrolledprogram = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
