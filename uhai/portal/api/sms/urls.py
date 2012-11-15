from django.conf.urls.defaults import * 
from views import send, new_message

urlpatterns = patterns('',
	(r'^cb/new-message/', new_message),
	(r'^cb/out-message/', out_message),
)