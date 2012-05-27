from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.utils.translation import ugettext

INSTALLED_APPS = (
	'admin_tools',
	'admin_tools.theming',
	'admin_tools.menu',
	'admin_tools.dashboard',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.admin',
	'django.contrib.markup',	
	'django.contrib.staticfiles',
	'uni_form',
	'wellness.userprofile',
	'wellness.core',	
	'wellness.programs',
	'wellness.insuranceprovider',
	'wellness.records',
	'wellness.patient',	
	'wellness.healthprovider',
	'wellness.medication',
	'wellness.questions',
	'wellness.reminders',
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "auth.email.EmailBackend"
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.request',	
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
)
