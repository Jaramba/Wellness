from django.conf.urls.defaults import *
from django.contrib import admin

from django.db.models.base import ModelBase
from django.views.generic.base import TemplateView

from wellness.core.utils import get_crud_urls

from models import *
from forms import *

urlpatterns = patterns('wellness.records.views',
    url(r'^$', 'index', name='records'),
)


urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
    models=[
       Encounter, Order, 
       Immunization, Problem, 
       TrackingField, Diagnosis, 
       ProblemTest, EncounterTest, 
       EncounterTestResult
    ],
    forms=[
       EncounterForm, OrderForm,
       ProblemForm, TrackingFieldForm,
       DiagnosisForm, ProblemTestForm, 
       EncounterTestForm, EncounterTestResultForm,
       ImmunizationForm
    ],
    data=globals()                            
)