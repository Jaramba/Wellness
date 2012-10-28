from django.conf.urls.defaults import * 

urlpatterns = patterns('uhai.portal.my.views',
    url(r'^/?$', 'switchboard', name='switchboard'),
)