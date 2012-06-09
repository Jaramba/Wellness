from django.conf.urls.defaults import *
from django.contrib import admin

from models import (PatientProgramQuestionnaire, ProgramQuestionnaire)
from django.db.models.base import ModelBase
from forms import (PatientProgramQuestionnaireForm)
from django.views.generic.base import TemplateView

from wellness.core.utils import get_crud_urls

urlpatterns = patterns('wellness.questions.views',
	url(r'^$', 'questionaire', {'action':'list', 'model_class':PatientProgramQuestionnaire}, name='questionnaire-list'),
	url(r'^response/$', 'responses', name='questionnaire-response'),
	url(r'(?P<questionnaire_pk>[-\d]+)/questionset/(?P<pk>[-\d]+)/$', 'questionset',{
			'action':'view',
			'template_name':'questions/questionset.html'
		}, 
	name='questionnaire-questionset'),
	url(r'(?P<pk>[-\d]+)/intro/$', 'questionaire_view',{
			'action':'view',
			'model_class':ProgramQuestionnaire,
			'template_name':'questions/questionnaire-intro-hero.html'
		}, 
	name='questionnaire-start'),
	url(r'(?P<pk>[-\d]+)/detail/$', 'questionaire_view', 
		{
			'action':'view',
			'model_class':ProgramQuestionnaire,
		}, 
	name='questionnaire-start'),
	url(r'(?P<pk>[-\d]+)/$', 'questionaire_view', 
		{
			'action':'view',
			'model_class':PatientProgramQuestionnaire,
			'template_name':'questions/questionnaire.html'
		}, 
	name='questionnaire-start'),
)