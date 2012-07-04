from django.conf.urls.defaults import *

from uhai.core.utils import get_crud_urls

from models import *
from forms import *

urlpatterns = patterns('uhai.reminders.views',
	url(r'^calendar/$', 'calendar', name="calendar"),
)

urlpatterns += get_crud_urls(
    '.'.join(__name__.split('.')[:-1]+['views']),models=[Event],forms=[EventForm],data=globals()                            
)