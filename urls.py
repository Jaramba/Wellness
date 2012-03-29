from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.base import TemplateView, RedirectView

from django.contrib.sites import models

from django.conf import settings

admin.autodiscover()

#django
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

#static website
urlpatterns += patterns('',
#    url(r'^privacy-policy/$', TemplateView.as_view(template_name='website/privacy_policy.html'), name="privacy-policy"),
)

#Acccount
urlpatterns += patterns('',
    # Registration
    url(r'^register/complete/$', TemplateView.as_view(template_name='userprofile/account/registration_done.html'),
        name='signup_complete'),
                        
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset',
        {'template_name': 'userprofile/account/password_reset.html',
         'email_template_name': 'userprofile/email/password_reset_email.txt' }, name='password_reset'),
                       
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'userprofile/account/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'userprofile/account/password_reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^password/reset/done/$',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'userprofile/account/password_reset_complete.html'}, name="password_reset_complete"),
)

#apps
urlpatterns += patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
)

#The app itself
urlpatterns += patterns('',
    url(r'^register/$', 'userprofile.views.register', {'template_name':'sign_up.html'},name='register'),
    url(r'^login/$', 'userprofile.views.login', {'template_name':'sign_in.html'}, name='login'),
    url(r'^logout/$','userprofile.views.logout', name='logout'),
    url(r'^upload/', include('fileuploader.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.MEDIA_ROOT, 'show_indexes': True}),
    )




