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

def get_crud_urls(views_module='', preurl='', posturl='', app_map={}, items=[], exclude=[]):
	'''
	This is an awesome magical URL creator... Meant for CRUD parts.
	Just pass a dictionary in the following form:
		'model_name':{
			'model':ModelItSelf,
			'forms':{
				'type_of_user': FormToGiveUser,
			},
			'actions':'CRUDL',#crud actions
		},
	'''

	url_patterns = []
	model_items = []
	urls = []

	'''
	if items:
		model_items=items
		
	elif exclude:		
		model_items = set(app_map.keys()) - set(exclude)
	'''
	
	for model_name, app_items in app_map.items():
		#app_items = app_map[model_name]
		qs = app_items['model'].objects.all()
		
		if 'C' in app_items['actions']:
			urls.append(url(r'^%s%s/create/%s$' % (preurl, model_name, posturl), model_name, {
					'action' : 'create','queryset':qs,'model_form_classes': app_items['forms'],
			}, name='%s-create' % model_name))
		if 'U' in app_items['actions']:
			urls.append(url(r'^%s%s/(?P<pk>[-\w]+)/edit/%s$' % (preurl, model_name, posturl), model_name, {
				'action' : 'edit',
				'queryset':qs,
				'model_form_classes': app_items['forms'],
			}, name='%s-edit' % model_name))
		if 'D' in app_items['actions']:
			urls.append(url(r'^%s%s/(?P<pk>[-\w]+)/delete/%s$' % (preurl, model_name, posturl), model_name, {'action' : 'delete', 'queryset':qs}, name='%s-delete' % model_name))
		if 'L' in app_items['actions']:
			urls.append(url(r'^%s%s/list/%s$' % (preurl, model_name, posturl), model_name, {'action' : 'list', 'queryset':qs}, name='%s-list' % model_name))
		if 'R' in app_items['actions']:
			urls.append(url(r'^%s%s/(?P<pk>[-\w]+)/%s$' % (preurl, model_name, posturl), model_name, {'action' : 'detail', 'queryset':qs}, name='%s-detail' % model_name))
		url_patterns += patterns(views_module, *urls)
	
	return url_patterns
