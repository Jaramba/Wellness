from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.utils.translation import ugettext

INSTALLED_APPS = (
	#admin
	'admin_tools',
	'admin_tools.theming',
	'admin_tools.menu',
	'admin_tools.dashboard',
	
	#django default
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.admin',
	'django.contrib.markup',	
	'django.contrib.staticfiles',
	'django.contrib.humanize',
	
	#apps
	'crispy_forms',
	'guardian',
	'messages',
	'pagination',
	#'south',
	
	'uhai.userprofile',
	'uhai.core',	
	'uhai.programs',
	'uhai.insuranceprovider',
	'uhai.records',
	'uhai.patient',	
	'uhai.healthprovider',
	'uhai.medication',
	'uhai.questions',
	'uhai.reminders',
	'uhai.userprofile',
	'uhai.stats',
	'uhai.sharer',
)

CRISPY_TEMPLATE_PACK = 'bootstrap'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
	"guardian.backends.ObjectPermissionBackend",
    "uhai.auth.email.EmailBackend",
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.request',	
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.request',
	'uhai.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'pagination.middleware.PaginationMiddleware',
)

ANONYMOUS_USER_ID = -1

SITE_NAME = 'UHAI'
META_KEYWORDS = ''
META_DESCRIPTION = ''

# Cookie name. This can be whatever you want.
SESSION_COOKIE_NAME = 'sessionid'
# The module to store sessions data.
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# Age of cookie, in seconds (default: 2 weeks).
SESSION_COOKIE_AGE = 60 * 60 * 24 * 2
# Whether a user's session cookie expires when the Web browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# Whether the session cookie should be secure (https:// only).
SESSION_COOKIE_SECURE = False
