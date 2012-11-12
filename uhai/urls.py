from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

	url(r'^$', 'uhai.portal.my.views.switchboard', name="home"),

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

urlpatterns += patterns('',	
    url(r'^about/$', TemplateView.as_view(template_name='website/how_it_works.html'), name="about"),
    url(r'^terms-of-service/$', TemplateView.as_view(template_name='website/terms-conditions.html'), name="terms_and_conditions"),
    url(r'^privacy-policy/$', TemplateView.as_view(template_name='website/privacy_policy.html'), name="privacy-policy"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.MEDIA_ROOT, 'show_indexes': True}),
    )
