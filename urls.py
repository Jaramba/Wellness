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
    url(r'^$', 'views.index', name="index"),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^records/', include('records.urls')),
    url(r'^providers/', include('healthprovider.urls')),
    url(r'', include('userprofile.urls')),
)

#Acccount
urlpatterns += patterns('',
    # Registration
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset',
        {'template_name': 'userprofile/account/password_reset.html', 'email_template_name': 'userprofile/email/password_reset_email.txt' }, name='password_reset'),
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'userprofile/account/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'userprofile/account/password_reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'userprofile/account/password_reset_complete.html'}, name="password_reset_complete"),
)
#The app itself
urlpatterns += patterns('',
    url(r'^register/$', 'userprofile.views.register', {'template_name':'sign_up.html'},name='register'),
    url(r'^login/$', 'userprofile.views.login', {'template_name':'sign_in.html'}, name='login'),
    url(r'^logout/$','userprofile.views.logout', name='logout'),
)

urlpatterns += patterns('',
    url(r'^messages/$', TemplateView.as_view(template_name='website/how_it_works.html'), name="messages"),
    url(r'^terms-of-service/$', TemplateView.as_view(template_name='website/terms-conditions.html'), name="terms_and_conditions"),
    url(r'^product-guide/$', TemplateView.as_view(template_name='website/product_guide.html'), name="product_guide"),
    url(r'^faqs/$', TemplateView.as_view(template_name='website/faqs.html'), name="faqs"),
    url(r'^privacy-policy/$', TemplateView.as_view(template_name='website/privacy_policy.html'), name="privacy-policy"),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.MEDIA_ROOT, 'show_indexes': True}),
    )




