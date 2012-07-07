from django.conf.urls.defaults import *

from uhai.core.utils import get_crud_urls

from models import *
from forms import *

urlpatterns = patterns('uhai.reminders.views',
	url(r'^calendar/$', 'calendar', name="calendar"),
)

VIEW_NAME = '.'.join(__name__.split('.')[:-1]+['views'])
APP_MAP={
	'event':{
		'model':Event,
		'forms':{
			'patient': EventForm,
		},
		'actions':'CRUDL',
	}, 
}

urlpatterns += get_crud_urls(
    VIEW_NAME,
	app_map=APP_MAP	
)