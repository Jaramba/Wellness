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

def get_crud_urls(views_module='', preurl='', posturl='', models=[], forms=[], data=globals(), actions=['C','R','U','D','L']):
    url_patterns = []
    for i,M in enumerate(models):
		qs = M.objects.all()
		model_name = M.__name__.lower()
		form_class = forms[i]
		urls = []
		if 'L' in actions:
			urls.append(url(r'^%s%s/list/%s$' % (preurl, model_name, posturl), model_name, {'action' : 'list', 'queryset':qs}, name='%s-list' % model_name))
		if 'C' in actions:
			urls.append(url(r'^%s%s/create/%s$' % (preurl, model_name, posturl), model_name, {
					'action' : 'create','queryset':qs,'model_form_class': form_class,
			}, name='%s-create' % model_name))
		if 'U' in actions:
			urls.append(url(r'^%s%s/(?P<pk>[-\w]+)/edit/%s$' % (preurl, model_name, posturl), model_name, {
				'action' : 'edit',
				'queryset':qs,
				'model_form_class': form_class,
			}, name='%s-edit' % model_name))
		if 'D' in actions:
			urls.append(url(r'^%s%s/(?P<pk>[-\w]+)/delete/%s$' % (preurl, model_name, posturl), model_name, {'action' : 'delete', 'queryset':qs}, name='%s-delete' % model_name))
		if 'D' in actions:
			urls.append(url(r'^%s%s/(?P<pk>[-\w]+)/%s$' % (preurl, model_name, posturl), model_name, {'action' : 'detail', 'queryset':qs}, name='%s-detail' % model_name))
		url_patterns += patterns(views_module,*urls)
    return url_patterns
