from django.conf.urls.defaults import *

from app_map import VIEW_NAME, APP_MAP

from uhai.core.utils import get_crud_urls

urlpatterns = patterns(VIEW_NAME,
    url(r'^$', 'index', name='programs'),
)

urlpatterns += get_crud_urls(
    VIEW_NAME,
	app_map=APP_MAP
)

'''
urlpatterns += patterns('uhai.programs.views',
	url(r'^questionnaires/$', 'questionaire', {'action':'list', 'queryset':Questionnaire.objects.all(),}, name='questionnaire-list'),
	url(r'^response/$', 'responses', name='questionnaire-response'),
	url(r'(?P<questionnaire_pk>[-\d]+)/questionset/(?P<pk>[-\d]+)/$', 'questionset',{
			'action':'view',
			'template_name':'questions/questionset.html'
		}, 
	name='questionnaire-questionset'),
	url(r'(?P<pk>[-\d]+)/intro/$', 'questionaire_view',{
			'action':'view',
			'queryset':Questionnaire.objects.all(),
			'template_name':'questions/questionnaire-intro-hero.html'
		}, 
	name='questionnaire-start'),
	url(r'(?P<pk>[-\d]+)/detail/$', 'questionaire_view', 
		{
			'action':'view',
			'queryset':Questionnaire.objects.all(),
		}, 
	name='questionnaire-start'),
	url(r'(?P<pk>[-\d]+)/$', 'questionaire_view', 
		{
			'action':'view',
			'queryset':Questionnaire.objects.all(),
			'template_name':'questions/questionnaire.html'
		}, 
	name='questionnaire-start'),
)
'''