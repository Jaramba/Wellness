###########################################################################
DEBUG = True 
TEMPLATE_DEBUG = DEBUG
###########################################################################
from settings import os, CURRENT_PATH  
###########################################################################

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME'      : 'ideasafrica_inp', # Or path to database file if using sqlite3.
        'HOST'      : '',                      # Set to empty string for localhost. Not used with sqlite3.
        'USER'      : 'ideasafrica_inp',
        'PORT'      : '',                      # Set to empty string for default. Not used with sqlite3.
        'PASSWORD'  : 'inposting90@210!',
 
    }
}