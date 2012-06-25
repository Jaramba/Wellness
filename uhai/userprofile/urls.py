from django.conf.urls.defaults import *
from django.conf import settings
from forms import *

from django.utils.functional import lazy
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('uhai.userprofile.views',
    # Private profile
	url(r'^settings/account/$', 'user_change', name='settings'),
    url(r'^settings/personal/$', 'personal', {'form':UserProfileForm}, name='settings-personal'),
	url(r'^settings/location/$', 'personal', {'form':LocationForm}, name='settings-location'),
    url(r'^settings/contacts/$', 'personal', {'form':ContactsForm}, name='settings-contacts'),
)

urlpatterns += patterns('',
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset',
        {'template_name': 'userprofile/password_reset.html'}, name='settings-password-reset'),
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done',
        {'template_name': 'userprofile/password_reset_done.html'}, name='password-reset-done'),
    url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'userprofile/password_reset_confirm.html'}, name="password-reset-confirm"),
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'userprofile/password_reset_complete.html'}, name="password-reset-complete"),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^settings/password/$', 'password_change',
        {
             'template_name': 'userprofile/password_change.html',
             'password_change_form':PasswordChangeForm,
             'post_change_redirect':reverse_lazy('settings-password-done'),
        }, 
        name='settings-password'
    ),
    url(r'^settings/password/done/$', 'password_change_done',
		{
			'template_name': 'userprofile/password_change_done.html'
		}, 
        name='settings-password-done'
    ),
)
