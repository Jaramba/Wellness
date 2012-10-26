from django.conf.urls.defaults import * 

urlpatterns = patterns('uhai.portal.core.sites',
    url(r'^/?$', 'switchboard', name='switchboard'),
)