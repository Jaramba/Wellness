from django.conf.urls.defaults import * 

urlpatterns = patterns('',    
    url(r'^stats/', include('uhai.portal.api.stats.urls')),
)