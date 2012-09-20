from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from django.conf import settings

from django.contrib.auth.decorators import login_required

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect

from django.template.context import RequestContext

from utils import has_permissions

def model_view(request, pk=None,
         template_name='',
         queryset=None,
         action='view',
         data = {},
         max_pagination_items=5,
         model_class=None,
         model_form_class=None,
         model_form_classes=[],
         initial_form_data={},
         save_form=lambda form, request=None, commit=False:form.save(request=request, commit=commit),
         redirect_to=None,
         redirect_to_args=[],
         extra_action=lambda request, action:None,
         context_object_name=lambda model_obj:model_obj._meta.object_name.lower(),
         context_object_name_plural=lambda model_obj:model_obj._meta.object_name.lower()+'s',
         context_form_name='form',
         extra_data={},
         *args,
         **kwargs):
           
    if not queryset:
        try:
            queryset = model_class.objects.by_request(request)
        except AttributeError, e:
            queryset =  model_class.objects.filter(site=settings.SITE_ID)

    success = False
    if action in ('detail','edit','delete', 'create', 'view'):
        try:
            model_obj = queryset.filter(pk=pk).get() if pk else queryset.model()
            if not has_permissions(request, model_obj, action):
                raise PermissionDenied
        except queryset.model.DoesNotExist:
            raise Http404('%s #%s does not exist' % (queryset.model._meta.verbose_name, pk or 0))
        except AssertionError, e:
            raise e
        data['object'] = data[context_object_name(model_obj) if callable(context_object_name) else context_object_name] = model_obj        
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
                    o = save_form(form, request=request)
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

def user_model_view(
    request, 
    user_pk=None,
    *args, 
    **kwargs):
    
    if not kwargs.get('queryset'):
        try:
            kwargs['queryset'] = kwargs['model_class'].objects.by_request(request)
        except AttributeError, e:
            kwargs['queryset'] =  kwargs['model_class'].objects.filter(site=settings.SITE_ID)
    
    if request.session.get('use_page_as') == 'patient':
        user = request.user
        kwargs['queryset'] = kwargs['queryset'].filter(model_owner=user)
    else:
        if user_pk:
            user = get_object_or_404(User, pk=user_pk)
            kwargs['queryset'] = kwargs['queryset'].filter(model_owner=user)
            if not kwargs.get('redirect_to'):
                kwargs['redirect_to_args'] = [user.pk]

    return model_view(request, *args, **kwargs)
    
def role_model_view(
    request,
    model_form_classes={},
    *args, 
    **kwargs):
        
    if kwargs['action'] in ('create', 'edit'):
        kwargs['model_form_class'] = model_form_classes.get(request.session.get('use_page_as') or 'patient', None)
        if not kwargs['model_form_class']:
            raise Http404("You're Forbidden from seeing this!")
                
    return user_model_view(request, *args, **kwargs) 

secured_model_view = login_required(lambda request, *args, **kwargs: model_view(request, *args, **kwargs))
secured_role_model_view = login_required(lambda request, *args, **kwargs: role_model_view(request, *args, **kwargs))
secured_user_model_view = login_required(lambda request, *args, **kwargs: user_model_view(request, *args, **kwargs))