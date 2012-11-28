from django.conf.urls.defaults import *

from app_map import VIEW_NAME, APP_MAP
from uhai.core.funcs import get_crud_urls

from django.views.generic.base import TemplateView
from models import Questionnaire, ProgramQuestionnaire, VitalsQuestionnaire
from forms import ProgramQuestionnaireForm

urlpatterns = patterns(VIEW_NAME,
    url(r'^$', 'index', name='programs'),
)

urlpatterns += get_crud_urls(
    VIEW_NAME,
	app_map=APP_MAP
)

urlpatterns += patterns("uhai.portal.my.programs.views",
	url(r"questionnaires/(?P<qtype>[-\w]+)/(?P<slug>[-\w]+)/entries/$", "questionnaire_entries", {'model':VitalsQuestionnaire}, name="vitals-questionnaire-entries"),
    url(r"questionnaires/(?P<qtype>[-\w]+)/(?P<slug>[-\w]+)/sent/$", "questionnaire_sent", name="questionnaire_sent"),
    url(r"questionnaires/(?P<qtype>[-\w]+)/(?P<slug>[-\w]+)/$", "questionnaire_detail", name="questionnaire_detail"),
)