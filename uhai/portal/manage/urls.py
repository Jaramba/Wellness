from django.conf.urls.defaults import * 
from django.contrib import admin
from views import send, new_message

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
