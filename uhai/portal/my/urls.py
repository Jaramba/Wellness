from django.conf.urls.defaults import * 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

	url(r'^/?$', 'uhai.portal.my.views.switchboard', name="index"),

    url(r'^reminders/', include('uhai.portal.my.reminders.urls')),
    url(r'^programs/', include('uhai.portal.my.programs.urls')),
    url(r'^medication/', include('uhai.portal.my.medication.urls')),

    url(r'^records/', include('uhai.portal.my.records.urls')),
    url(r'^providers/', include('uhai.portal.my.providers.urls')),
    url(r'^insurance/', include('uhai.portal.my.insurance.urls')),
    url(r'^records/', include('uhai.portal.my.patients.urls')),


    #?P<scheme_slug>\w+
    
    url(r'^search/', include('uhai.portal.my.search.urls')),        

	url(r'^login/?$', 'uhai.portal.my.userprofile.views.login', {
    		'template_name':'userprofile/login.html'
    	}, name='login'
    ),
    url(r'^logout/?$','uhai.portal.my.userprofile.views.logout', {
    		'redirect_field_name':'next',
    		'template_name':'userprofile/logout.html'
    	}, name='logout'
    ),

    url(r'', include('uhai.portal.my.userprofile.urls')),
    url(r'', include('uhai.core.urls')),
)	