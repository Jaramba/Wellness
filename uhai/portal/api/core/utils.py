from base64 import b32encode
from hashlib import sha1
from random import random

from django.contrib.auth.decorators import user_passes_test
from django.conf.urls.defaults import *

from django.utils.translation import ugettext, ugettext_lazy as _

from uhai.portal.sites.insurance.models import HealthInsuranceProvider

from django.conf import settings

def insurance_site_callback(request, scheme_slug=None):
    request.current_insurance = get_object_or_404(HealthInsuranceProvider, slug=scheme_slug)

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

def delete_selected(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    app_label = opts.app_label

    # Check that the user has delete permission for the actual model
    if not modeladmin.has_delete_permission(request):
        raise PermissionDenied

    using = router.db_for_write(modeladmin.model)

    # Populate deletable_objects, a data structure of all related objects that
    # will also be deleted.
    deletable_objects, perms_needed, protected = get_deleted_objects(
        queryset, opts, request.user, modeladmin.admin_site, using)

    # The user has already confirmed the deletion.
    # Do the deletion and return a None to display the change list view again.
    if request.POST.get('post'):
        if perms_needed:
            raise PermissionDenied
        n = queryset.count()
        if n:
            for obj in queryset:
                obj_display = force_unicode(obj)
                modeladmin.log_deletion(request, obj, obj_display)
            for o in queryset:
                o.delete(request=request)
            modeladmin.message_user(request, _("Successfully deleted %(count)d %(items)s.") % {
                "count": n, "items": model_ngettext(modeladmin.opts, n)
            })
        # Return None to display the change list page again.
        return None

    if len(queryset) == 1:
        objects_name = force_unicode(opts.verbose_name)
    else:
        objects_name = force_unicode(opts.verbose_name_plural)

    if perms_needed or protected:
        title = _("Cannot delete %(name)s") % {"name": objects_name}
    else:
        title = _("Are you sure?")

    context = {
        "title": title,
        "objects_name": objects_name,
        "deletable_objects": [deletable_objects],
        'queryset': queryset,
        "perms_lacking": perms_needed,
        "protected": protected,
        "opts": opts,
        "app_label": app_label,
        'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
    }

    # Display the confirmation page
    return TemplateResponse(request, modeladmin.delete_selected_confirmation_template or [
        "admin/%s/%s/delete_selected_confirmation.html" % (app_label, opts.object_name.lower()),
        "admin/%s/delete_selected_confirmation.html" % app_label,
        "admin/delete_selected_confirmation.html"
    ], context, current_app=modeladmin.admin_site.name)

delete_selected.short_description = _("Delete selected %(verbose_name_plural)s")

				
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
        acl = obj.access_control_list
        if acl:
            return acl.get('system', acl.get(request.user.username, {})).get(action, False)
            
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
