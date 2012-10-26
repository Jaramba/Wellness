from django.conf.urls.defaults import * 

urlpatterns = patterns('',
	url(r'^/?$', 'uhai.views.dashboard', name="index"),
    url(r'^search/', include('uhai.search.urls')),    

	url(r'^reminders/', include('uhai.reminders.urls')),
	url(r'^programs/', include('uhai.programs.urls')),
	url(r'^medication/', include('uhai.medication.urls')),

    url(r'^records/', include('uhai.records.urls')),
	url(r'^providers/', include('uhai.providers.urls')),
	url(r'^insurance/', include('uhai.insurance.urls')),
	url(r'^records/', include('uhai.patients.urls')),

	url(r'', include('uhai.core.urls')),
	url(r'', include('uhai.userprofile.urls')),
)	