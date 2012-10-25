PARENT_HOST   = 'uhai.co.ke'

DEBUG = True
TEMPLATE_DEBUG = DEBUG 

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