from django_hosts import patterns, host
from django.conf import settings

from django.contrib import admin

host_patterns = patterns('',
	host(r'www', 	settings.ROOT_URLCONF, 		name='default'),
	host(r'api', 	'uhai.portal.api.urls', 	name='api'),
    host(r'my', 	'uhai.portal.patient.urls', name='my-portal'),#patient portal
    host(r'doctors','uhai.portal.providers.urls', name='doctor-portal'),#doctors portal
    host(r'admin', 	'uhai.portal.manage.urls', 	name='admin-portal'),#insurance management portal
    host(r'(\w+)', 	'uhai.portal.sites.urls', 	name='insurance-sites'),
)