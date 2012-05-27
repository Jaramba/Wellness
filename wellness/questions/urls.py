from django.conf.urls.defaults import *
from django.contrib import admin

from models import (PatientProgramQuestionnaire)
from django.db.models.base import ModelBase
from forms import (PatientProgramQuestionnaireForm)
from django.views.generic.base import TemplateView

from wellness.core.utils import get_crud_urls

urlpatterns = patterns('',
)

urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
    models=[
       PatientProgramQuestionnaire
    ],
    forms=[
       PatientProgramQuestionnaireForm
    ],
    data=globals()                            
)