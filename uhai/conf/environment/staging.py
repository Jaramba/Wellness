from django.conf import settings
import os

print "Name"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PARENT_HOST   = 'uhai.synacor.co.ke'

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