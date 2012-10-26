from django.conf.urls.defaults import *

urlpatterns = patterns('uhai.portal.my.search.views',
	url(r'^$', 'index', name="search-index"),
	url(r'^$', 'index', name="search-suggestions"),
	url(r'^filter/(?P<section>[-\w]+)/$', 'filter', name="filter-index"),
)