from django.conf.urls.defaults import *
from django.contrib import admin

from django.db.models.base import ModelBase
from django.views.generic.base import TemplateView

from uhai.core.utils import get_crud_urls

from models import *
from forms import *

urlpatterns = patterns('uhai.records.views',
    url(r'^$', 'index', name='records'),
)

urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
	preurl='patient/(?P<patient_number>[-\w]+)/',
    models=[
       Encounter, Order, 
       Immunization,  
       TrackingField, Diagnosis,
       ProblemTest, EncounterTest, 
       EncounterTestResult
    ],
    forms=[
       EncounterPatientForm, OrderForm,
	   ImmunizationForm,
       ProblemForm, TrackingFieldForm,
       DiagnosisForm, ProblemTestForm, 
       EncounterTestForm, EncounterTestResultForm,
    ],
    data=globals()                            
)

urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
    models=[
       Encounter, Order, 
       Immunization,  
       TrackingField, Diagnosis, 
       ProblemTest, EncounterTest, 
       EncounterTestResult
    ],
    forms=[
       EncounterForm, OrderForm,
	   ImmunizationForm,
       ProblemForm, TrackingFieldForm,
       DiagnosisForm, ProblemTestForm, 
       EncounterTestForm, EncounterTestResultForm,
    ],
    data=globals()                            
)