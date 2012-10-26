from django.conf.urls.defaults import * 

urlpatterns = patterns('',
	url(r'^/?$', 'uhai.portal.my.views.switchboard', name="index"),
    url(r'^search/', include('uhai.search.urls')),    

	url(r'^reminders/', include('uhai.reminders.urls')),
	url(r'^programs/', include('uhai.programs.urls')),
	url(r'^medication/', include('uhai.medication.urls')),

    url(r'^records/', include('uhai.records.urls')),
	url(r'^providers/', include('uhai.providers.urls')),
	url(r'^insurance/', include('uhai.insurance.urls')),
	url(r'^records/', include('uhai.patients.urls')),

	url(r'^login/?$', 'uhai.userprofile.views.login', {
    		'template_name':'userprofile/login.html'
    	}, name='login'
    ),
    url(r'^logout/?$','uhai.userprofile.views.logout', {
    		'redirect_field_name':'next',
    		'template_name':'userprofile/logout.html'
    	}, name='logout'
    ),

	url(r'', include('uhai.core.urls')),
	url(r'', include('uhai.userprofile.urls')),
)	