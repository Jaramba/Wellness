from django.conf.urls.defaults import *

from uhai.core.funcs import get_crud_urls
from app_map import VIEW_NAME, APP_MAP

urlpatterns = patterns('uhai.portal.my.reminders.views',
	url(r'^calendar/$', 'calendar', name="calendar"),
)

urlpatterns += get_crud_urls(
    VIEW_NAME,
	app_map=APP_MAP	
)