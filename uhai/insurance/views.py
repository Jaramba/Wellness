# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required
from uhai.core.views import model_view

patientinsurance = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
healthinsuranceprovider = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
insurance = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
employercompany = login_required(lambda request, *args, **kwargs: model_view(request, context_object_name_plural=lambda obj:"companies", *args, **kwargs))
