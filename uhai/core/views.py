from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect

from django.template.context import RequestContext
from django.forms.models import modelform_factory

def model_view(request, pk=None,
         template_name='',
         queryset=None,
         action='view',
         data = {},
		 max_pagination_items=5,
		 model_form_class=[],
		 model_form_classes=[],
         initial_form_data={},
         save_form=lambda form, commit=False:form.save(),
		 redirect_to=None,
         redirect_to_args=[],
         extra_action=lambda request, action:None,
         context_object_name=lambda model_obj:model_obj._meta.object_name.lower(),
         context_object_name_plural=lambda model_obj:model_obj._meta.object_name.lower()+'s',
         context_form_name='form',
         extra_data={}):
	
	success = False
	if action in ('detail','edit','delete', 'create', 'view'):
		try:
			model_obj = queryset.filter(pk=pk).get() if pk else queryset.model()
		except queryset.model.DoesNotExist:
			raise Http404('%s #%s does not exist' % (queryset.model._meta.verbose_name, pk))
		except AssertionError, e:
			raise e
		data['object'] = data[context_object_name(model_obj) if callable(context_object_name) else context_object_name] = model_obj
		
		if action in ('edit', 'create'):
			if not model_form_class:
				model_form_class = modelform_factory(queryset.model)
	else:		
		page = request.REQUEST.get('page', 1)
		paginator = Paginator(queryset, max_pagination_items)
		
		try:
			objects = paginator.page(page)
		except PageNotAnInteger:
			objects = paginator.page(1)
		except EmptyPage:
			objects = paginator.page(paginator.num_pages)
		
		data['objects'] = data[context_object_name_plural(queryset.model) if callable(context_object_name_plural) else context_object_name_plural] = objects
		
	if not template_name:
		if action == "delete":
			template_name = "delete_base.html"
		else:
			template_name = "%s/%s_%s.html" % (queryset.model._meta.app_label, queryset.model._meta.object_name.lower(), action)
	
	if request.method == 'GET':
		if action in ['create', 'view', 'edit', 'delete', 'list']:
			if action in ['create', 'edit']:
				data[context_form_name] = model_form_class(initial=initial_form_data) if action == 'create' else model_form_class(instance=model_obj, initial=initial_form_data)
		else:
			extra_action(request, action)
		
	elif request.method == 'POST':
		if action == 'edit' or action == 'create':	
			model_form_classes.append(model_form_class)
				
			for model_form_class in model_form_classes:
				form = model_form_class(request.POST, request.FILES, instance=model_obj)
				if form.is_valid():
					o = save_form(form)
					success = True

			if success:
				return redirect(redirect_to) if redirect_to else redirect('%s-list' % queryset.model.__name__.lower(), *redirect_to_args)
			data[context_form_name] = form
		elif action == 'delete':
			if model_obj:
				model_obj.delete()
			return redirect('%s-list' % queryset.model.__name__.lower())
		else:
			extra_action(request, action)
			
	data.update(extra_data)
	return render_to_response(template_name, data, context_instance=RequestContext(request))

def role_model_view(
	request,
	model_form_classes={},
	*args, 
	**kwargs):
	
	if kwargs['action'] in ('create', 'edit'):
		kwargs['model_form_class'] = model_form_classes.get(request.session.get('use_page_as') or 'patient', None)
		
	return model_view(request, *args, **kwargs)

def user_model_view(
	request, 
	user_pk=None,
	*args, 
	**kwargs):	
	
	if request.session.get('use_page_as') == 'patient':
		user = request.user
		kwargs['queryset'] = kwargs['queryset'].filter(user=user)
		if not kwargs.get('redirect_to'):
			kwargs['redirect_to_args'] = [user.pk]
	else:
		if user_pk:
			user = get_object_or_404(User, pk=user_pk)
			kwargs['queryset'] = kwargs['queryset'].filter(user=user)
			if not kwargs.get('redirect_to'):
				kwargs['redirect_to_args'] = [user.pk]
			
	return role_model_view(request, *args, **kwargs)
