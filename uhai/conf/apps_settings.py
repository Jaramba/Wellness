from django.conf import settings

INSTALLED_APPS = [
	#admin
	'admin_tools',
	'admin_tools.theming',
	'admin_tools.menu',
	'admin_tools.dashboard',
	
	#django default
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.admin',
	'django.contrib.markup',	
	'django.contrib.staticfiles',
	'django.contrib.humanize',
	
	#apps
	'crispy_forms',
    'cloudinary',
	
	# API Tools
    'tastypie',
    
	#Search Tools
    'haystack',
    'celery_haystack',
    'saved_searches',
	
	#Database tools
	#'south',
	
	#Customer Care...
	'intercom',
		
	'uhai.core',
	'uhai.portal.sites.programs',
	'uhai.portal.sites.insurance',
	'uhai.portal.sites.records',
	'uhai.portal.sites.patients',	
	'uhai.portal.sites.providers',
	'uhai.portal.sites.medication',
	'uhai.portal.sites.reminders',
	'uhai.portal.my.userprofile',	
	'uhai.portal.api.stats',
	'uhai.portal.api.sms',
	'uhai.portal.sites.sharer',
]

QUESTIONNAIRE_BUILDER_UPLOAD_TO = UPLOAD_TO = 'formsbuilder_uploads'
# Nay
QUESTIONNAIRE_BUILDER_EMAIL_TO = EMAIL_TO = None
# The maximum allowed length for field values.
QUESTIONNAIRE_BUILDER_FIELD_MAX_LENGTH = FIELD_MAX_LENGTH = 2000
# The maximum allowed length for field labels.
QUESTIONNAIRE_BUILDER_LABEL_MAX_LENGTH = LABEL_MAX_LENGTH = 200
# The absolute path where files will be uploaded to.
QUESTIONNAIRE_BUILDER_UPLOAD_ROOT = UPLOAD_ROOT = None
# Boolean controlling whether HTML5 questionnaire fields are used.
QUESTIONNAIRE_BUILDER_USE_HTML5 = USE_HTML5 = True
# Boolean controlling whether forms are associated to Django's Sites framework.
QUESTIONNAIRE_BUILDER_USE_SITES = USE_SITES = 'django.contrib.sites' in INSTALLED_APPS
# Boolean controlling whether questionnaire slugs are editable in the admin.
QUESTIONNAIRE_BUILDER_EDITABLE_SLUGS = EDITABLE_SLUGS = False
# Char to start a quoted choice with.
QUESTIONNAIRE_BUILDER_CHOICES_QUOTE = CHOICES_QUOTE = '`'
# Char to end a quoted choice with.
QUESTIONNAIRE_BUILDER_CHOICES_UNQUOTE = CHOICES_UNQUOTE = '`'
# Char to use as a field delimiter when exporting questionnaire responses as CSV.
QUESTIONNAIRE_BUILDER_CSV_DELIMITER = CSV_DELIMITER = ','
# Boolean controlling whether emails to staff recipients are sent from the questionnaire submitter.
SEND_FROM_SUBMITTER = True

CRISPY_TEMPLATE_PACK = 'bootstrap'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'uhai.auth.email.EmailBackend',
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

MIDDLEWARE_CLASSES = [
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
]

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
