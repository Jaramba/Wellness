# Django settings for wellness project.
import os
from django.utils.translation import ugettext_lazy as _

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))

ADMINS = (
    ('ONESMUS MUKEWA', 'kanarelo@gmail.com'),
)


# debug-toolbar settings
INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

############################--DATABASES--###############################################
USE_SQLITE = True

try:
    from database_dev import *
except:
    from database_prod import *
    
########################################################################################

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

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(CURRENT_PATH, '..','templates'),
)

LOCALE_PATHS = (
    os.path.join(CURRENT_PATH, '..','locale'),
)

#for testing purposes:
LOGIN_URL = '/login/'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

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

from apps_settings import *
from extra_settings import *
from static_media_settings import *
