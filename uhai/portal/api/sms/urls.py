from django.conf.urls.defaults import * 
from views import send, new_message

urlpatterns = patterns('',
    (r'^send/', send),
	(r'^cb/new-message/', new_message),
)