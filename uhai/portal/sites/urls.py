from django.conf.urls.defaults import * 

urlpatterns = patterns('uhai.portal.my',
    url(r'^/?$', 'switchboard', name='switchboard'),
)