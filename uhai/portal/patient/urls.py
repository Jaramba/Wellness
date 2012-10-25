from django.conf.urls.defaults import * 
from views import send, new_message

urlpatterns = patterns('',
    url(r'^search/', include('uhai.search.urls')),		
    
	url(r'', include('uhai.core.urls')),
	url(r'', include('uhai.userprofile.urls')),
)	