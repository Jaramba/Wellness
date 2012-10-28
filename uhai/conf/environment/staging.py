from django.conf import settings
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PARENT_HOST   = 'uhai.synacor.co.ke'

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