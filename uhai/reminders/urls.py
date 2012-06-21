from django.conf.urls.defaults import *
from models import *
from forms import *

urlpatterns = patterns('uhai.reminders.views',
	url(r'^calendar/$', 'calendar', name="calendar"),
)