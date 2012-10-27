from django.conf import settings

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.views import login as auth_login, logout as auth_logout

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _

from django.views.decorators.http import require_GET
from django.views.generic.base import TemplateView

if settings.STAGE == "staging":
    from django_hosts.reverse_full import reverse_full
else:
    from django.core.urlresolvers import reverse
    reverse_full = lambda hostname, url, *args, **kwargs: reverse(url, *args, **kwargs)

from forms import *
from signals import *

import copy

def login(request, *args, **kwargs):
    if not request.user.is_authenticated():
		if request.method == 'POST':
			if not request.POST.get('remember', None):
				request.session.set_expiry(0)
		return auth_login(
                request, 
                authentication_form=AuthenticationForm, 
                *args, **kwargs
        )
    else:
        return HttpResponseRedirect(reverse_full('my-portal', 'index'))

def logout(request, user_type="applicant", template_name=None, *args, **kwargs):
    if request.user.is_authenticated():
		if request.method == "GET":
			return render_to_response(template_name, {}, context_instance=RequestContext(request)) 
		elif request.method == "POST":
			return auth_logout(request, *args, **kwargs)
    else:
        return HttpResponseRedirect(reverse_full('my-portal', "login"))

@login_required
@require_GET
def public(request, user_id=None, template_name="userprofile/public.html"):
    data = {}
    
    user = user=get_object_or_404(User, pk=user_id)
    profile, created = UserProfile.objects.get_or_create(user=user)
    
    if not (request.user == profile.user):
        profile.views += 1
        profile.save()
    else:
        pass
        
    data['profile'] = profile
    
    return render_to_response(template_name, data, context_instance=RequestContext(request)) 

from uhai.core.views import model_view
@login_required
def user_change(request):
    data = {}
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserForm(instance=request.user)

    template = "userprofile/personal.html"
    data['form'] = form
    return render_to_response(template, data, context_instance=RequestContext(request))

@login_required
def personal(request, selected="profile", form=None):
    """
    UserProfileal data of the user profile
    """
    
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    data = {}
    data["selected"] = selected
    data["profile"] = profile
    
    ProfileForm = form
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=profile)

    template = "userprofile/personal.html"
    data['form'] = form
    return render_to_response(template, data, context_instance=RequestContext(request))

@login_required
def delete(request):
    data = {}

    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        patch_profile(request.user, profile)
        
        old_profile = copy.copy(profile)
        old_user    = copy.copy(request.user)

        # Remove the profile and all the information
        UserProfile.objects.filter(user=request.user).delete()
        
        # Remove the e-mail of the account too
        request.user.email = ''
        request.user.first_name = ''
        request.user.last_name = ''
        request.user.save()

        messages.success(request, _("Your profile information has been removed successfully."), fail_silently=True)

        signal_responses = signals.post_signal.send(sender=delete, request=request, extra={'old_profile':old_profile, 'old_user': old_user})
        return signals.last_response(signal_responses) or HttpResponseRedirect(reverse_full("my-portal", "profile_overview"))

    template = "userprofile/delete.html"
    data.update({ 'section': 'delete' })
    signals.context_signal.send(sender=delete, request=request, context=data)
    return render_to_response(template, data, context_instance=RequestContext(request))

def register(request, template_name=None):
    if not request.user.is_authenticated():
        data = {}
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                
                iam = request.POST.get("i_am","applicant")
                
                if iam and iam == "applicant":
                    user.groups.add(Group.objects.get(name__iexact='Applicant'))
                    #add to starter package in units app
                    starter_package_name = getattr(settings, 'DEFAULT_USER_PACKAGE', 'starter')
                    starter_package = UserPackage.objects.get_or_create(name=starter_package_name)[0]
                    user_credit = UserCredit(user=user,
                                             credit_balance=starter_package.initial_balance,
                                             package=starter_package)
                    user_credit.save()
                else:
                    user.groups.add(Group.objects.get(name__iexact='Recruiter'))

                user.save()
                
                profile = UserProfile(user=user, default_dashboard=iam)
                profile.save()
                
                return login(request, template_name="sign_in.html")
        else:
            form = RegistrationForm()
        
        data['form'] = form
        return render_to_response(template_name, data, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse_full("default", 'index'))
