from base64 import b32encode
from hashlib import sha1
from random import random

from django.contrib.auth.decorators import user_passes_test
from django.conf.urls.defaults import *

def pkgen():
    rude = ('lol',)
    bad_pk = True
    
    while bad_pk:
        pk = b32encode(sha1(str(random())).digest()).lower()[:9]
        bad_pk = False
        for rw in rude:
            if pk.find(rw) >= 0:
                bad_pk = True
                return pk

def perform_raw_sql(sql, data=[]):
	from django.db import connection, transaction
	cursor = connection.cursor()
	cursor.execute(sql, data)
	transaction.commit_unless_managed()

def get_crud_urls(views_module='', models=[], forms=[], data=globals()):
    url_patterns = []  
    for M in models:
        model_name = M.__name__.lower()
        form_class = data[M.__name__+'Form'] 
        url_patterns += patterns(views_module,
            url(r'^%s/list/$' % model_name, model_name, {'action' : 'list', 'model_class':M}, name='%s-list' % model_name),
            url(r'^%s/create/$' % model_name, model_name, {
                'action' : 'create',
                'model_class':M,
                'model_form_class': form_class,
            }, name='%s-create' % model_name),
            url(r'^%s/(?P<pk>[-\w]+)/edit/$' % model_name, model_name, {
                'action' : 'edit',
                'model_class':M,
                'model_form_class': form_class,
            }, name='%s-edit' % model_name),
            url(r'^%s/(?P<pk>[-\w]+)/delete/$' % model_name, model_name, {'action' : 'delete', 'model_class':M}, name='%s-delete' % model_name),
            url(r'^%s/(?P<pk>[-\w]+)/$' % model_name, model_name, {'action' : 'detail', 'model_class':M}, name=' %s-detail' % model_name),
        )
    return url_patterns
