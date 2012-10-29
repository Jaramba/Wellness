from django.conf.urls.defaults import * 

urlpatterns = patterns('',
	url(r'^/?$', 'uhai.portal.my.views.switchboard', name="index"),
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
)	