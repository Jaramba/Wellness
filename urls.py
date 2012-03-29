from conf.settings import *
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView, RedirectView
from views import *
from taggit.views import tagged_object_list

from django.contrib.sites import models
from django.utils.functional import lazy

admin.autodiscover()

reverse_lazy = lazy(reverse, str)

#django
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

#static website
urlpatterns += patterns('',
    url(r'^about/$', TemplateView.as_view(template_name='website/about.html'), name="about"),
    url(r'^how-it-works/$', TemplateView.as_view(template_name='website/how_it_works.html'), name="how_it_works"),
    url(r'^resources/$', TemplateView.as_view(template_name='website/resources.html'), name="resources"),
    url(r'^what-it-is/$', TemplateView.as_view(template_name='website/what_it_is.html'), name="what_it_is"),
    url(r'^terms-of-service/$', TemplateView.as_view(template_name='website/terms-conditions.html'), name="terms_and_conditions"),
    url(r'^rewards/$', TemplateView.as_view(template_name='website/rewards.html'), name="rewards"),
    url(r'^product-guide/$', TemplateView.as_view(template_name='website/product_guide.html'), name="product_guide"),
    url(r'^faqs/$', TemplateView.as_view(template_name='website/faqs.html'), name="faqs"),
    url(r'^privacy-policy/$', TemplateView.as_view(template_name='website/privacy_policy.html'), name="privacy-policy"),
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
    url(r'^tags/(?P<slug>[-\w]+)/$', tagged_object_list, name='tags'),
)

#The app itself
urlpatterns += patterns('',
    url(r'^$', index, name="index"),
    url(r'^choose-user-type/$', choose_usertype, name="choose-usertype"),
    
    url(r'^recruit/', include('recruit.urls')),
    url(r'', include('applicant.urls')),
    
    url(r'^register/$', 'userprofile.views.register', {'template_name':'sign_up.html'},name='register'),
    url(r'^login/$', 'userprofile.views.login', {'template_name':'sign_in.html'}, name='login'),
    url(r'^logout/$','userprofile.views.logout', {"next_page":reverse_lazy("index")}, name='logout'),

    url(r'^emailconfirmation/', include('emailconfirmation.urls')),
    url(r'', include('social.urls')),
)

urlpatterns += patterns('',
    url(r'', include('userprofile.urls')),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^messages/', include('inbox.urls')),
)

urlpatterns += patterns('',
    url(r'^units/', include('units.urls')),
)
#matcher app
urlpatterns += patterns('',
    url(r'^matcher/', include('matcher.urls')),
    url(r'^upload/', include('fileuploader.urls')),
)

if DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root' :STATIC_ROOT}),
        (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root' : MEDIA_ROOT, 'show_indexes': True}),
    )




