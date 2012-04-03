from django.conf import settings

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.views import login as auth_login, logout as auth_logout

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _

from django.views.decorators.http import require_GET
from django.views.generic.base import TemplateView

from forms import *
from signals import *

import copy

def login(request, *args, **kwargs):
    if not request.user.is_authenticated():
        return auth_login(request, *args, **kwargs)
    else:
        return HttpResponseRedirect(reverse('index'))

def logout(request, type=None, user_type="applicant", *args, **kwargs):
    if request.user.is_authenticated():
        return auth_logout(request, *args, **kwargs)
    else:
        return HttpResponseRedirect(reverse("login"))

class RegistrationCompleteTemplateView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(RegistrationCompleteTemplateView, self).get_context_data(**kwargs)
        context.update({
            'email_validation_required': (hasattr(settings, "REQUIRE_EMAIL_CONFIRMATION") and settings.REQUIRE_EMAIL_CONFIRMATION)
        })
        return context

@login_required
@require_GET
def public(request, user_id=None, template_name="userprofile/profile/public.html"):
    data = {}
    
    user = user=get_object_or_404(User, pk=user_id)
    profile, created = UserProfile.objects.get_or_create(user=user)
    
    if not (request.user == profile.user):
        profile.views+=1
        profile.save()
        
    if is_applicant(request.user) and not is_recruiter(request.user):
        data['base_template'] = "applicant_base.html"
        form = ApplicantForm
    elif is_recruiter(request.user):
        data['base_template'] = "recruit_base.html"
    else:
        pass
        
    data['profile'] = profile
    
    return render_to_response(template_name, data, context_instance=RequestContext(request)) 

@login_required
def company(request, company_slug=None, selected="profile"):
    data = {}
    data["company"] = company = get_object_or_404(Company, pk=request.session.get('current_company', ''))
    
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
    else:
        form = CompanyForm(instance=company)
        
    template = "userprofile/profile/company_profile.html"
    data.update({ 'section': 'personal', 'form': form, 'type':'company', 'selected': 'profile'})
    return render_to_response(template, data, context_instance=RequestContext(request))

@login_required
def personal(request, selected="profile"):
    """
    Personal data of the user profile
    """
    
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    data = {}
    data["selected"] = selected
    data["profile"] = profile
    data['base_template'] = "applicant_base.html"
    
    ProfileForm = UserProfileForm
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            if full_name:
                full_name_to_user(request.user, full_name)
                request.user.save()
            form.save()
    else:
        form = ProfileForm(
            initial={
                'first_name':request.user.first_name,
                'last_name':request.user.last_name,
                'email': request.user.email
            },
            instance=profile
        )

    template = "userprofile/profile/personal.html"
    data.update({ 'section': 'personal', 'form': form, })
    return render_to_response(template, data, context_instance=RequestContext(request))

@login_required
def delete(request):
    data = {}

    profile, created = UserProfile.objects.get_or_create(user=request.user)
    #if is_applicant(request.user) and not is_recruiter(request.user):
    #    data['base_template'] = "applicant_base.html"
    #    data['student'] = profile
    #elif is_recruiter(request.user):
    #    data['base_template'] = "recruit_base.html"
    #    data['recruiter'] = profile
    #else:
    #    pass
    
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
        return signals.last_response(signal_responses) or HttpResponseRedirect(reverse("profile_overview"))

    template = "userprofile/profile/delete.html"
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
        return HttpResponseRedirect(reverse('index'))
