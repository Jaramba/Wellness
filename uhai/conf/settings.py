# Django settings for uhai project.
import os
from django.utils.translation import ugettext_lazy as _

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('ONESMUS MUKEWA', 'kanarelo@gmail.com'),
)

# debug-toolbar settings
INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

SITE_ID = 1

from django.conf.global_settings import LANGUAGES 

LANGUAGES += (
    ('sw', _('Swahili')),
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@tn-2-e9$r@=wy54+7g3b#-i(c8xf_-h5!0j!!4l3^q!dw6z^='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF  = 'uhai.portal.www.urls'
ROOT_HOSTCONF = 'uhai.hosts'
DEFAULT_HOST  = 'default'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STAGE = os.environ.get('STAGE', 'staging')
# Load settings specified by STAGE environment variable


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
    
    #Database tools
    #'south',
    
    #Customer Care...
    'intercom',
        
    'uhai.core',
    'uhai.portal.my.programs',
    'uhai.portal.my.insurance',
    'uhai.portal.my.records',
    'uhai.portal.my.patients',   
    'uhai.portal.my.providers',
    'uhai.portal.my.medication',
    'uhai.portal.my.reminders',
    'uhai.portal.my.userprofile',   
    'uhai.portal.api.stats',
    'uhai.portal.api.sms',
    'uhai.portal.my.sharer',
]

#Search Settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__),'..', '..', 'whoosh_index'),
    },
}

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'uhai.auth.email.EmailBackend',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request',   
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'uhai.core.context_processors.request',
]

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


