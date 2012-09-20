from base64 import b32encode
from hashlib import sha1
from random import random

from django.contrib.auth.decorators import user_passes_test
from django.conf.urls.defaults import *

from django.conf import settings

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

def has_permissions(request, obj=None, action=None):
    '''
    If the User is the owner... Let him at it...
    If the Usrt is the Super User, Let him at it...
    Else, check the group, and finally the check at the ACL...
    '''
    if obj:
        if (request.user == obj.model_owner) or request.user.is_superuser:
            return True
        #TODO:Check if the Person's Group belongs to this site...
        #Also, check if the User Group level is granular; can a doctor prescribe
        #Someone else's patient.... Lovely.

        if obj.access_control_list:
            return obj.access_control_list \
                .get(request.user.username, {}).get(action, False)
            
    return False
    

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
	urls = []
	model_items = app_map.keys()

	if items:
		model_items=items
	elif exclude:		
		model_items = set(model_items) - set(exclude)
	
	for model_name in model_items:
		app_items = app_map[model_name]
		
		if 'C' in app_items['actions']:
			urls.append(url(r'^%s%s/create/%s$' % (preurl, model_name, posturl), 
			'%s.%s' % (views_module, app_items.get('view', 'secured_role_model_view')), {
					'action' : 'create', 'model_class':app_items.get('model'), 'model_form_classes': app_items['forms'],
			}, name='%s-create' % model_name))
		
		if 'L' in app_items['actions']:
			urls.append(url(r'^%s%s/list/%s$' % (preurl, model_name, posturl), 
			'%s.%s' % (views_module, app_items.get('view', 'secured_model_view')), {
					'action' : 'list', 
					'model_class':app_items.get('model')
				}, name='%s-list' % model_name)
			)
		if 'U' in app_items['actions']:
			urls.append(url(r'^%s%s/(?P<pk>[-\d]+)/edit/%s$' % (preurl, model_name, posturl), 
			'%s.%s' % (views_module, app_items.get('view', 'secured_role_model_view')), {
				'action' : 'edit',
				'model_class':app_items.get('model'),
				'model_form_classes': app_items['forms'],
			}, name='%s-edit' % model_name))
		if 'D' in app_items['actions']:
			urls.append(url(r'^%s%s/(?P<pk>[-\d]+)/delete/%s$' % (preurl, model_name, posturl), 
			'%s.%s' % (views_module, app_items.get('view', 'secured_model_view')), {'action' : 'delete', 'model_class':app_items.get('model')}, name='%s-delete' % model_name))
		
		if 'R' in app_items['actions']:
			urls.append(url(r'^%s%s/(?P<pk>[-\d]+)/%s$' % (preurl, model_name, posturl), 
			'%s.%s' % (views_module, app_items.get('view', 'secured_model_view')), {'action' : 'detail', 'model_class':app_items.get('model')}, name='%s-detail' % model_name))
		
		url_patterns += patterns('', *urls)
	return url_patterns
