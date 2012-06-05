#development settings
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
		'NAME': 'c:/Users/ian/Documents/GitHub/Wellness/wellness/database/wellness.db', 
		'HOST': '', 
		'USER': '', 
		'PASSWORD': '', 
		'PORT': ''
	}
}