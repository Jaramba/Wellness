from django.conf.urls.defaults import *
from django.contrib import admin

from django.db.models.base import ModelBase
from forms import *
from django.views.generic.base import TemplateView

from wellness.core.utils import get_crud_urls

urlpatterns = patterns('',
)

urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
    models=[
        Program, 
        EnrolledProgram,
    ],
    forms=[
        ProgramForm, 
        EnrolledProgramForm
    ],
    data=globals()                            
)   