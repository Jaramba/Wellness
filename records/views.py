# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import *
from forms import * 
from django.views.generic.create_update import create_object
from django.contrib.auth.decorators import login_required

def model_view(request, pk=None, 
         template_name='', 
         model_obj=None, 
         queryset=None,
         model_class=None, 
         model_form_class=None, 
         action='view',
         data = {},
         save_form=lambda form:form.save(),
         redirect_to=lambda model_class:'%s-detail' % model_class._meta.object_name.lower(),
         extra_action=lambda request, action:None,
         context_object_name=lambda model_obj:model_obj._meta.object_name.lower(),
         context_object_name_plural=lambda model_obj:model_obj._meta.object_name.lower()+'s',
         context_form_name='form',
         extra_data={}):
    
    if action in ('view','edit','delete', 'create'):
        if not model_obj and (model_class and pk):
            model_obj = get_object_or_404(model_class, pk=pk)
        elif model_class and not pk:
            model_obj = model_class()
        data[context_object_name] = model_obj
    else:
        if not queryset and model_class:
            queryset = model_class.objects.filter()
            data[context_object_name_plural] = queryset
    
    if not template_name:
        model = queryset.model if queryset else model_class 
        template_name = "%s/%s_%s.html" % (model._meta.app_label, model._meta.object_name.lower(), action)
    create_object
        
    if request.method == 'GET':
        if action in ['create', 'detail', 'edit', 'delete', 'list']:
            if action in ['create', 'edit', 'delete']:
                data[context_form_name] = form = model_form_class()
        else:
            extra_action(request, action)
        
    elif request.method == 'POST':
        if action == 'edit' or action == 'create':
            if model_form_class:
                form = model_form_class(request.POST, request.FILES, instance=model_obj)
                if form.is_valid():
                    save_form(form)
                    return HttpResponseRedirect(reverse(callable(redirect_to) and redirect_to() or redirect_to))
                data[context_form_name] = form
        elif action == 'delete':
            if model_obj:
                model_obj.delete()
        else:
            extra_action(request, action)
            
    data.update(extra_data)
    return render_to_response(template_name, data, context_instance=RequestContext(request))

def encounter(request, *args, **kwargs):
    wrapped = login_required(model_view)
    kwargs['model_form_class'] = EncounterForm
    return wrapped(request, *args, **kwargs)

def order(request, *args, **kwargs):
    wrapped = login_required(model_view)
    kwargs['model_form_class'] = EncounterForm
    return wrapped(request, *args, **kwargs)

def problem(request, *args, **kwargs):
    wrapped = login_required(model_view)
    kwargs['model_form_class'] = EncounterForm
    return wrapped(request, *args, **kwargs)

def visit(request, *args, **kwargs):
    wrapped = login_required(model_view)
    kwargs['model_form_class'] = EncounterForm
    return wrapped(request, *args, **kwargs)

def immunization(request, *args, **kwargs):
    wrapped = login_required(model_view)
    kwargs['model_form_class'] = EncounterForm
    return wrapped(request, *args, **kwargs)
