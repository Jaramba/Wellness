from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

def model_view(request, pk=None, 
         template_name='',
         queryset=None,
         model_form_class=None,
         model_form_classes=[],
         action='view',
         data = {},
         initial_form_data=lambda:{},
         save_form=lambda form:form.save(),
         redirect_to=None,
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
			raise Http404()
		except AssertionError, e:
			raise e
		data[context_object_name(model_obj)] = model_obj
		print data
	else:
		data[context_object_name_plural(queryset.model)] = queryset

	if not template_name:
		template_name = "%s/%s_%s.html" % (queryset.model._meta.app_label, queryset.model._meta.object_name.lower(), action)
		
	if request.method == 'GET':
		if action in ['create', 'view', 'edit', 'delete', 'list']:
			if action in ['create', 'edit']:
				data[context_form_name] = model_form_class() if action == 'create' else model_form_class(instance=model_obj)
		else:
			extra_action(request, action)
		
	elif request.method == 'POST':
		if action == 'edit' or action == 'create':
			model_form_classes.append(model_form_class)
				
			for model_form_class in model_form_classes:  
				print request.POST
				form = model_form_class(request.POST, request.FILES, instance=model_obj)
				if form.is_valid():
					o = save_form(form)
					success = True
			
			if success:
				return HttpResponseRedirect(reverse('%s-list' % queryset.model.__name__.lower()))
			data[context_form_name] = form
		elif action == 'delete':
			if model_obj:
				model_obj.delete()
		else:
			extra_action(request, action)
			
	data.update(extra_data)
	return render_to_response(template_name, data, context_instance=RequestContext(request))
