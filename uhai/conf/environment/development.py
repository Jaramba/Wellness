from uhai.conf.settings import *
import os

PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),'..','..')

ROOT_URLCONF  = 'uhai.portal.my.urls'

PARENT_HOST   = 'localhost'

#development settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG
CRISPY_FAIL_SILENTLY = DEBUG

# e-mail settings
DEFAULT_FROM_EMAIL = 'noreply@uhai.com'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'uhai'
EMAIL_HOST_PASSWORD = 'a79fHH7722!'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'dev_templates'),
)

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', 
		'NAME': os.path.join(PROJECT_PATH, 'database', 'uhai.db'), 
		'HOST': '', 
		'USER': '', 
		'PASSWORD': '', 
		'PORT': ''
	}
}

SIMPLE_API_URL = "https://simple.majisoft.co.ke/"

#Debug Settings
#Middleware
MIDDLEWARE_CLASSES += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INSTALLED_APPS += [
    "debug_toolbar",
    #"devserver",
]

DEBUG_TOOLBAR_CONFIG = {
	'INTERCEPT_REDIRECTS' : not DEBUG,
	'SHOW_TEMPLATE_CONTEXT' : DEBUG,
	'ENABLE_STACKTRACES' : DEBUG,
}

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    'haystack.panels.HaystackDebugPanel',
)

DEVSERVER_ARGS = [
    "--dozer",
]

DEVSERVER_IGNORED_PREFIXES = [
    "/site_media/",
]

DEVSERVER_MODULES = [
    # "devserver.modules.sql.SQLRealTimeModule",
    "devserver.modules.sql.SQLSummaryModule",
    "devserver.modules.profile.ProfileSummaryModule",

    # Modules not enabled by default
    "devserver.modules.ajax.AjaxDumpModule",
    "devserver.modules.cache.CacheSummaryModule",
    "devserver.modules.profile.LineProfilerModule",
]

#New Relic Monitoring :)
NEW_RELIC_EXTENSIONS_ENABLED = not DEBUG
NEW_RELIC_EXTENSIONS_DEBUG = not NEW_RELIC_EXTENSIONS_ENABLED
NEW_RELIC_EXTENSIONS_ATTRIBUTES = {
    'user': {
        'username': 'Django username',
    },
    'is_secure': 'Django secure conneciton',
    'REQUEST': 'Django Request Variable'
}

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'templates'),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale'),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, '..', 'static_root')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'static'),
)
