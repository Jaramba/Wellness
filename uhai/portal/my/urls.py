from django.conf.urls.defaults import * 

urlpatterns = patterns('',
	url(r'^/?$', 'uhai.portal.my.views.switchboard', name="index"),
    url(r'^search/', include('uhai.portal.my.search.urls')),    

	url(r'^reminders/', include('uhai.portal.sites.reminders.urls')),
	url(r'^programs/', include('uhai.portal.sites.programs.urls')),
	url(r'^medication/', include('uhai.portal.sites.medication.urls')),

    url(r'^records/', include('uhai.portal.sites.records.urls')),
	url(r'^providers/', include('uhai.portal.sites.providers.urls')),
	url(r'^insurance/', include('uhai.portal.sites.insurance.urls')),
	url(r'^records/', include('uhai.portal.sites.patients.urls')),

	url(r'^login/?$', 'uhai.portal.my.userprofile.views.login', {
    		'template_name':'userprofile/login.html'
    	}, name='login'
    ),
    url(r'^logout/?$','uhai.portal.my.userprofile.views.logout', {
    		'redirect_field_name':'next',
    		'template_name':'userprofile/logout.html'
    	}, name='logout'
    ),

	url(r'', include('uhai.utils.urls')),
	url(r'', include('uhai.portal.my.userprofile.urls')),
)	