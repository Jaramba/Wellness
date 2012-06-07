from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

#django
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

#apps
urlpatterns += patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="landing-page"),
	url(r'^home/$', 'wellness.views.index', name="index"),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^stats/', include('wellness.stats.urls')),
    url(r'^records/', include('wellness.records.urls')),
    url(r'^providers/', include('wellness.healthprovider.urls')),
    url(r'^employee-programs/', include('wellness.programs.urls')),
    url(r'^insurance/', include('wellness.insuranceprovider.urls')),
    url(r'^medications/', include('wellness.medication.urls')),
	url(r'^patients/', include('wellness.patient.urls')),
    url(r'^programs/', include('wellness.programs.urls')),
    url(r'^questionnaires/', include('wellness.questions.urls')),
    url(r'', include('wellness.core.urls')),
    url(r'', include('wellness.userprofile.urls')),
)

#The app itself
urlpatterns += patterns('',
    url(r'^login/$', 'wellness.userprofile.views.login', {'template_name':'userprofile/login.html'}, name='login'),
    url(r'^logout/$','wellness.userprofile.views.logout', {'redirect_field_name':'next','template_name':'userprofile/logout.html'}, name='logout'),
)

urlpatterns += patterns('',
    url(r'^about/$', TemplateView.as_view(template_name='website/how_it_works.html'), name="messages"),
    url(r'^terms-of-service/$', TemplateView.as_view(template_name='website/terms-conditions.html'), name="terms_and_conditions"),
    url(r'^privacy-policy/$', TemplateView.as_view(template_name='website/privacy_policy.html'), name="privacy-policy"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.MEDIA_ROOT, 'show_indexes': True}),
    )
