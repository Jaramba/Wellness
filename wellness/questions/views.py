# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required
from wellness.core.views import model_view

patientprogramquestionnaire = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
