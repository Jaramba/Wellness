from django.conf.urls.defaults import *

from models import *
from forms import *

urlpatterns = patterns('uhai.portal.my.sharer.views',
	url(r'^request/(?P<app_label>[-\w]+)/(?P<model>[-\w]+)/$', 'sharer', name="request-sharer"),
	url(r'^requests/?$', 'sharer', {'action':'list', 'template_name':'userprofile/sharerequests.html'}, name="share-request"),
)