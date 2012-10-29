from django.conf.urls.defaults import * 

urlpatterns = patterns('uhai.portal.sites.views',
    url(r'^/?$', 'switchboard', name='switchboard'),

    url(r'^reminders/', include('uhai.portal.sites.reminders.urls')),
	url(r'^programs/', include('uhai.portal.sites.programs.urls')),
	url(r'^medication/', include('uhai.portal.sites.medication.urls')),

    url(r'^records/', include('uhai.portal.sites.records.urls')),
	url(r'^providers/', include('uhai.portal.sites.providers.urls')),
	url(r'^insurance/', include('uhai.portal.sites.insurance.urls')),
	url(r'^records/', include('uhai.portal.sites.patients.urls')),

	url(r'', include('uhai.core.urls')),
	url(r'', include('uhai.portal.my.userprofile.urls')),
)