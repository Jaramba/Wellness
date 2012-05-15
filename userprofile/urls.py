from django.conf.urls.defaults import *
from views import *
from django.conf import settings
from forms import *
from django.utils.functional import lazy
from django.contrib.auth.views import password_change

reverse_lazy = lazy(reverse, str)

urlpatterns = patterns('',
    # Private profile
    url(r'^settings/$', personal, {'selected':'profile'}, name='settings'),
    url(r'^settings/password/?$', password_change,
        {
             'template_name': 'userprofile/account/password_change.html',
             'password_change_form':PasswordChangeForm,
             'post_change_redirect':reverse_lazy('settings-password-done'),
             'extra_context':{
                'base_template':'applicant_base.html',
                'selected':'password', 
             }
        }, 
        name='settings-password'
    ),
    url(r'^settings/password/done/$', 
        password_change,
        {
             'template_name': 'userprofile/account/password_change.html',
             'password_change_form':PasswordChangeForm, 
             'extra_context':{
                    'base_template':'applicant_base.html',
                    'selected':'password',
            }
         }, 
        name='settings-password-done'
    ),
)
