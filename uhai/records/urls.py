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
	preurl='patient/(?P<patient_pk>[-\w]+)/',
    models=[
       Encounter, Order, 
       TrackingField,
       Diagnosis, ProblemTest, 
	   EncounterTest, 
       EncounterTestResult
    ],
    forms=[
       EncounterPatientForm, OrderForm,
       TrackingFieldForm,
       DiagnosisForm, ProblemTestForm, 
       EncounterTestForm, EncounterTestResultForm,
    ],
    data=globals()                            
)

urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
	posturl='type/(?P<problem_type>[-\w]+)/',
    models=[
       Diagnosis,
    ],
    forms=[
       DiagnosisForm
    ],
    data=globals()
)

urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
	posturl='type/(?P<encounter_type>[-\w]+)/',
    models=[
       Encounter,
    ],
    forms=[
       EncounterForm
    ],
    data=globals()
)

urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
    models=[
       Encounter, Order, 
       TrackingField,
       Diagnosis, ProblemTest, 
	   EncounterTest, 
       EncounterTestResult
    ],
    forms=[
       EncounterPatientForm, OrderForm,
       TrackingFieldForm,
       DiagnosisForm, ProblemTestForm, 
       EncounterTestForm, EncounterTestResultForm,
    ],
    data=globals()                            
)