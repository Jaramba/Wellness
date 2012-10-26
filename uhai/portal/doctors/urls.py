from django.conf.urls.defaults import * 
from views import send, new_message

urlpatterns = patterns('',
    url(r'sms/', include('uhai.portal.api.sms.urls')),
)