from django.conf.urls.defaults import *
from django.contrib import admin

from models import (Prescription, Medication, Immunization)
from django.db.models.base import ModelBase
from forms import (PrescriptionForm, MedicationForm, ImmunizationForm)
from django.views.generic.base import TemplateView

from uhai.core.utils import get_crud_urls

urlpatterns = patterns('',
)

urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
	preurl='patient/(?P<patient_pk>[-\w]+)/',
    models=[
       Prescription,
	   Immunization, 
    ],
    forms=[
       PrescriptionForm,
	   ImmunizationForm,
    ],
    data=globals()                            
)


urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
    models=[
       Prescription, 
	   Medication,
	   Immunization,  
    ],
    forms=[
       PrescriptionForm, 
	   MedicationForm,
	   ImmunizationForm,
    ],
    data=globals()                            
)