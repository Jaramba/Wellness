from django.conf.urls.defaults import *

from app_map import VIEW_NAME, APP_MAP
from uhai.portal.api.core.utils import get_crud_urls

from django.views.generic.base import TemplateView
from models import Questionnaire, ProgramQuestionnaire
from forms import ProgramQuestionnaireForm

urlpatterns = patterns(VIEW_NAME,
    url(r'^$', 'index', name='programs'),
)

urlpatterns += get_crud_urls(
    VIEW_NAME,
	app_map=APP_MAP
)

urlpatterns += patterns("uhai.portal.sites.programs.views",
    url(r"questionaires/(?P<slug>[-\w]+)/sent/$", "questionnaire_sent", name="questionnaire_sent"),
    url(r"questionaires/(?P<slug>[-\w]+)/$", "questionnaire_detail", {
        'QuestionnaireType': ProgramQuestionnaire, 'QuestionnaireTypeForm': ProgramQuestionnaireForm, 
    }, name="questionnaire_detail"),
)