from django.conf.urls.defaults import *
from django.conf import settings
from forms import *

from uhai.portal.my.patients.forms import Patient, PatientProfileForm

from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('uhai.portal.my.userprofile.views',
    # Private profile
    url(r'^profile/(?P<pk>[0-9A-Za-z]+)?/?$', 'profile', {"contact":ContactsForm, "password":PasswordChangeForm}, name='profile'),
	url(r'^settings/$', 'user_change', name='settings'),
    url(r'^personal/$', 'personal', {'form':UserProfileForm}, name='settings-personal'),
	url(r'^location/$', 'personal', {'form':LocationForm}, name='settings-location'),
    url(r'^contacts/$', 'personal', {'form':ContactsForm}, name='settings-contacts'),

    url(r'^login/?$', 'login', {
            'template_name':'userprofile/login.html'
        }, name='login'
    ),
    url(r'^logout/?$','logout', {
            'redirect_field_name':'next',
            'template_name':'userprofile/logout.html'
        }, name='logout'
    ),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^password/$', 'password_change',
        {
             'template_name': 'userprofile/password_change.html',
             'password_change_form':PasswordChangeForm,
             'post_change_redirect':reverse_lazy('settings-password-done'),
        }, 
        name='settings-password'
    ),
    url(r'^password/done/$', 'password_change_done',
        {
            'template_name': 'userprofile/password_change_done.html'
        }, 
        name='settings-password-done'
    ),
)

urlpatterns += patterns('uhai.portal.my.patients.views',
	url(r'^medical/$', 'patient', {
		'action' : 'edit',
		'template_name':'userprofile/personal.html',
		'queryset': Patient.objects.all(),
		'model_form_classes': {
			'patient': PatientProfileForm,
		},
		'redirect_to' : '/account/medical/'
	},	
	name='settings-medical'),
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
