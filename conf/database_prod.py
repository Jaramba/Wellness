###########################################################################
DEBUG = False
TEMPLATE_DEBUG = DEBUG
###########################################################################
from settings import os, CURRENT_PATH  
###########################################################################

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME'      : '~/webapp_releases/uhai/shared/database/wellness.db', # Or path to database file if using sqlite3.
        'HOST'      : '',                      # Set to empty string for localhost. Not used with sqlite3.
        'USER'      : '',
        'PORT'      : '',                      # Set to empty string for default. Not used with sqlite3.
        'PASSWORD'  : '',
 
    }
}
