from django.conf import settings
from django_hosts.reverse import reverse_full
from django.utils.functional import lazy
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

PARENT_HOST   = 'uhai.synacor.co.ke'
ROOT_HOSTCONF = 'uhai.hosts'
DEFAULT_HOST  = 'default'

print "HERE >>>>>>>> ", ROOT_HOSTCONF

reverse_lazy = lazy(reverse_full, unicode)
LOGIN_REDIRECT_URL = reverse_lazy('my-portal', 'index')
LOGIN_URL = reverse_lazy('my-portal', 'login')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(settings.CURRENT_PATH, '..','templates'),
)

settings.INSTALLED_APPS += [
	#Domain Tools
	'django_hosts',
]

settings.MIDDLEWARE_CLASSES += [
    'django_hosts.middleware.HostsMiddleware',
]

# e-mail settings
DEFAULT_FROM_EMAIL = 'noreply@uhai.com'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'uhai'
EMAIL_HOST_PASSWORD = 'a79fHH7722!'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', 
		'NAME': '/home/uhai/webapp_releases/uhai/shared/database/uhai.db', 
		'HOST': '', 
		'USER': '', 
		'PASSWORD': '', 
		'PORT': ''
	}
}

#Search Settings
HAYSTACK_CONNECTIONS = {
	'default': {
		'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
		'PATH': os.path.join(os.path.dirname(__file__),'..', '..', 'whoosh_index'),
	},
}
