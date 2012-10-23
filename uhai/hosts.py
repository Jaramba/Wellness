from django_hosts import patterns, host
from django.conf import settings

from django.contrib import admin

host_patterns = patterns('uhai',
	host(r'www', settings.ROOT_URLCONF, name='default'),
    host(r'admin', admin.urls, name='dmin'),
    host(r'my', 'uhai.portal.patient.urls', name='myportal'),#patient portal
    host(r'doctors', 'uhai.portal.providers.urls', name='doctors'),#doctors portal
    host(r'manage', 'uhai.portal.manage.urls', name='myportal'),#insurance management portal
    host(r'(\w+)', 'uhai.portal.sites.urls', name='insurance-sites'),
)