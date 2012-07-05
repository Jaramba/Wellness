from django.conf.urls.defaults import *

urlpatterns = patterns('uhai.search.views',
	url(r'^$', 'index', name="search-index"),
)