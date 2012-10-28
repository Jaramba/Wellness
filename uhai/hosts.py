from django_hosts import patterns, host
from django.conf import settings

from django.contrib import admin

host_patterns = patterns('',
	host(r'www', 	settings.ROOT_URLCONF, 		name='default'),
	host(r'api', 	'uhai.portal.api.urls', 	name='api'),
    host(r'my', 	'uhai.portal.my.urls', 		name='my-portal'),#main portal
    host(r'doctors','uhai.portal.providers.urls', name='doctor-portal'),#doctors portal
    host(r'admin', 	'uhai.portal.admin.urls', 	name='admin-portal'),#insurance management portal
    host(r'(?P<scheme_slug>\w+)', 
    	'uhai.portal.sites.urls', 
    	callback='uhai.portal.sites.insurance.models.insurance_site_callback', 
        name='insurance-sites'),
)