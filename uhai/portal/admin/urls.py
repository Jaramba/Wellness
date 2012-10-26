from django.conf.urls.defaults import * 
from django.contrib import admin

urlpatterns = patterns('',
    url(r'', include(admin.site.urls)),

    url(r'^admin_tools/', include('admin_tools.urls')),
)
