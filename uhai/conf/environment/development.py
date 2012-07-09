#development settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG
CRISPY_FAIL_SILENTLY = DEBUG

# e-mail settings
DEFAULT_FROM_EMAIL = 'noreply@uhai.com'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'uhai'
EMAIL_HOST_PASSWORD = 'a79fHH7722!'

from uhai.conf.settings import CURRENT_PATH, INSTALLED_APPS, MIDDLEWARE_CLASSES

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', 
		'NAME': CURRENT_PATH + '/../database/uhai.db', 
		'HOST': '', 
		'USER': '', 
		'PASSWORD': '', 
		'PORT': ''
	}
}

'''
INSTALLED_APPS += (
	'devserver',
)

MIDDLEWARE_CLASSES += (
    'devserver.middleware.DevServerMiddleware',
)

DEVSERVER_IGNORED_PREFIXES = [
	'/media', 
	'/uploads',
	'/static'
]

DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # Modules not enabled by default
    'devserver.modules.ajax.AjaxDumpModule',
    #'devserver.modules.profile.MemoryUseModule',
    'devserver.modules.cache.CacheSummaryModule',
    #'devserver.modules.profile.LineProfilerModule',
)

DEVSERVER_TRUNCATE_SQL = False
DEVSERVER_AUTO_PROFILE = True
DEVSERVER_AJAX_CONTENT_LENGTH = 300
'''