from django.conf.urls.defaults import * 

urlpatterns = patterns('',
    url(r'sms/', include('uhai.portal.api.sms.urls')),
    url(r'^stats/', include('uhai.portal.api.stats.urls')),
)