from django.conf.urls.defaults import *
from django.contrib import admin

from models import (
    ProgramType, Program, 
    ProgramWorkflow, ProgramWorkflowState,
    EnrolledProgram
)
from django.db.models.base import ModelBase
from forms import (
    ProgramTypeForm, ProgramForm, 
    ProgramWorkflowForm, ProgramWorkflowStateForm,
    EnrolledProgramForm
)
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
)

for M in (
    ProgramType, Program, 
    ProgramWorkflow, ProgramWorkflowState,
    EnrolledProgram):
    #The app itself
    model_name = M.__name__.lower()
    form_class = globals()[M.__name__+'Form'] 
    urlpatterns += patterns('wellness.programs.views',
        url(r'^%s/list/$' % model_name, model_name, {'action' : 'list', 'model_class':M}, name='%s-list' % model_name),
        url(r'^%s/create/$' % model_name, model_name, {
                        'action' : 'create',
                        'model_class':M,
                        'model_form_class': form_class,
                        }, name='%s-create' % model_name),
        url(r'^%s/(?P<pk>[-\w]+)/edit/$' % model_name, model_name, {
                        'action' : 'edit',
                        'model_class':M,
                        'model_form_class': form_class,
                        }, name='%s-edit' % model_name),
        url(r'^%s/(?P<pk>[-\w]+)/delete/$' % model_name, model_name, {'action' : 'delete', 'model_class':M}, name='%s-delete' % model_name),
        url(r'^%s/(?P<pk>[-\w]+)/$' % model_name, model_name, {'action' : 'detail', 'model_class':M}, name=' %s-detail' % model_name),
    )
    