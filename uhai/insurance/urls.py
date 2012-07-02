from django.conf.urls.defaults import *
from django.contrib import admin

from models import (EmployerCompany, HealthInsuranceProvider, Insurance, PatientInsurance)
from django.db.models.base import ModelBase
from forms import (EmployerCompanyForm, HealthInsuranceProviderForm, InsuranceForm, PatientInsuranceForm)
from django.views.generic.base import TemplateView

from uhai.core.utils import get_crud_urls

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='website/how_it_works.html'),name='providers'),
)

urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
    models=[
       EmployerCompany, 
	   HealthInsuranceProvider, 
       Insurance, 
	   PatientInsurance
    ],
    forms=[
       EmployerCompanyForm, 
	   HealthInsuranceProviderForm, 
       InsuranceForm, 
	   PatientInsuranceForm
    ],
    data=globals()                            
)