from django.conf.urls.defaults import * 

urlpatterns = patterns('',
    url(r'sms/', include('uhai.sms.urls')),
    url(r'^stats/', include('uhai.stats.urls')),
)