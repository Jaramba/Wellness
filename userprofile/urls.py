from django.conf.urls.defaults import *
from views import *
from django.conf import settings
from forms import *
from django.utils.functional import lazy
from django.contrib.auth.views import password_change

reverse_lazy = lazy(reverse, str)

urlpatterns = patterns('',
    # Private profile
    url(r'^profile/$', personal, {'selected':'profile'}, name='settings'),
    url(r'^profile/(?P<user_id>[-\d]+)/$', public, name='public-profile'),
    url(r'^profile/company/$', company, {'selected':'profile'}, name='company-settings'),
    url(r'^profile/social/$', personal, {'selected':'social'}, name='settings-social-accounts'),
    url(r'^profile/company/password/?$', password_change,
        {
             'template_name': 'userprofile/account/password_change.html',
             'password_change_form':PasswordChangeForm,
             'post_change_redirect':reverse_lazy('settings-password-done'),
             'extra_context':{
                'base_template':'recruit_base.html',
                'selected':'password',
                'type':'company', 
             }
        }, 
        name='settings-company-password'
    ),
    url(r'^profile/company/password/done/$', 
        password_change,
        {
             'template_name': 'userprofile/account/password_change.html',
             'password_change_form':PasswordChangeForm, 
             'extra_context':{
                    'base_template':'recruit_base.html',
                    'selected':'password',
                    'type':'company',
            }
         }, 
        name='settings-company-password-done'
    ),
    url(r'^profile/applicant/password/?$', password_change,
        {
             'template_name': 'userprofile/account/password_change.html',
             'password_change_form':PasswordChangeForm,
             'post_change_redirect':reverse_lazy('settings-password-done'),
             'extra_context':{
                'base_template':'applicant_base.html',
                'selected':'password', 
                'type':'applicant',
             }
        }, 
        name='settings-applicant-password'
    ),
    url(r'^profile/applicant/password/done/$', 
        password_change,
        {
             'template_name': 'userprofile/account/password_change.html',
             'password_change_form':PasswordChangeForm, 
             'extra_context':{
                    'base_template':'applicant_base.html',
                    'selected':'password',
                    'type':'applicant',
            }
         }, 
        name='settings-applicant-password-done'
    ),
)
