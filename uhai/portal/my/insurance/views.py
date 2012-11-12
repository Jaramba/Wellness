# Create your views here.
from models import *
from forms import * 
from django.contrib.auth.decorators import login_required
from uhai.core.views import *

employercompany = login_required(lambda request, *args, **kwargs: model_view(request, context_object_name_plural=lambda obj:"companies", *args, **kwargs))

@login_required
def patientinsurance(request, data={}, *args, **kwargs):
	kwargs['queryset'] = PatientInsurance.objects.filter(patient=request.user.patient_set.get())
	return model_view(request, extra_data=data, *args, **kwargs)