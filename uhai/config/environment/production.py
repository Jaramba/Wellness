from uhai.config.settings import *
import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)),'..','..'))
PARENT_HOST   = 'uhai-app.cloudapp.net'

DJANGO_SETTINGS_MODULE = 'uhai.config.environment.production'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += [
    'djcelery',
    'djsupervisor',
]

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3', 
#         'NAME': '/home/uhai/webapp_releases/uhai/shared/database/uhai.db', 
#         'HOST': '', 
#         'USER': '', 
#         'PASSWORD': '', 
#         'PORT': ''
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'uhai', 
        'HOST': 'localhost', 
        'USER': 'root', 
        'PASSWORD': 'mkemonda90@210!', 
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
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, '..', 'static'))

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'static'),
)

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

REDIS = {
    "default": {
        "HOST": "localhost",
        "PORT": "6379",
        "PASSWORD": "synacor90@210!666-heaven"
    }
}

RABBITMQ = {
    "default": {
        "HOST": "localhost",
        "USER": "admin",
        "PORT": "5672",
        "PASSWORD": "synacor90201",
    }
}

BROKER_HOST = RABBITMQ["default"]["HOST"]
BROKER_PORT = RABBITMQ["default"]["PORT"]
BROKER_USER = RABBITMQ["default"]["USER"]
BROKER_PASSWORD = RABBITMQ["default"]["PASSWORD"]
BROKER_VHOST = "/"

BROKER_POOL_LIMIT = 10

os.environ["CELERY_LOADER"] = "django"

CELERYD_CONCURRENCY = 1
CELERYD_NODES="w1"

CELERY_RESULT_BACKEND="amqp"

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31556926
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

#SECRET_KEY = os.environ.get("SECRET_KEY")

#EMAIL_HOST = os.environ.get("EMAIL_HOST")
#EMAIL_PORT = int(os.environ.get("EMAIL_PORT"))
#EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
#EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
#EMAIL_USE_TLS = True