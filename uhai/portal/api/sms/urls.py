from django.conf.urls.defaults import * 
from views import out_message, new_message

urlpatterns = patterns('',
	(r'^cb/new-message/', new_message),
	(r'^cb/out-message/', out_message),
)