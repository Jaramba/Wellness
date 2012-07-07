from django.conf.urls.defaults import *

from uhai.core.utils import get_crud_urls
from app_map import VIEW_NAME, APP_MAP

urlpatterns = patterns(VIEW_NAME,
    url(r'^$', 'index', name='records'),
)

urlpatterns += get_crud_urls(
    VIEW_NAME,
	app_map=APP_MAP	
)

urlpatterns += get_crud_urls(
    VIEW_NAME,
 	app_map=APP_MAP,
 	preurl='patient/(?P<patient_pk>[-\w]+)/'	
)

urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
 	posturl='type/(?P<problem_type>[-\w]+)/',
	app_map=APP_MAP,
    items=['diagnosis']	
)

urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),
	posturl='type/(?P<encounter_type>[-\w]+)/',
    app_map=APP_MAP,
    items=['encounter']
)
