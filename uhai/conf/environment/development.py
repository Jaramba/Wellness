#development settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG
CRISPY_FAIL_SILENTLY = DEBUG

# e-mail settings
DEFAULT_FROM_EMAIL = 'noreply@uhai.com'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'uhai'
EMAIL_HOST_PASSWORD = 'a79fHH7722!'

import os
from django.conf import settings

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', 
		'NAME': settings.CURRENT_PATH + '/../database/uhai.db', 
		'HOST': '', 
		'USER': '', 
		'PASSWORD': '', 
		'PORT': ''
	}
}

#Search Settings
HAYSTACK_CONNECTIONS = {
	'default': {
		'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
		'PATH': os.path.join(os.path.dirname(__file__),'..', '..', 'whoosh_index'),
	},
}

SIMPLE_API_URL = "https://simple.majisoft.co.ke/"

#Debug Settings
#Middleware
settings.MIDDLEWARE_CLASSES += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

settings.INSTALLED_APPS += [
    "debug_toolbar",
    "devserver",
]

print settings.INSTALLED_APPS

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