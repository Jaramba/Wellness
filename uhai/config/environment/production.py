from uhai.config.settings import *
import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)),'..','..'))
PARENT_HOST   = 'uhai-app.cloudapp.net'

DEBUG = True
TEMPLATE_DEBUG = DEBUG 


INSTALLED_APPS += [
    'gunicorn',
]

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

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(PROJECT_PATH,'templates')),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH,'locale'),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH,'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, '..', 'static_root'))

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'static'),
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

CONFIG = {
    'mode': 'django',
    'environment': {
        'PYTHONPATH': '/home/uhai/webapps/uhai/wellness/',
    },
    # 'working_dir': '/',
    'user': 'www-data',
    'group': 'www-data',
    'args': (
        '--bind=127.0.0.1:8000',
        '--workers=4',
        '--log-level=debug',
        '--log-file=/home/uhai/webapps/uhai/logs/uhai.log',
        '--worker-class=egg:gunicorn#sync',
        '--timeout=30',
        'settings',
    ),
}
