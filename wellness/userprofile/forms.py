from django import forms
from django.contrib.auth.forms import PasswordChangeForm as _PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from models import *
import re

class RegistrationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and password.
    """
    username = forms.CharField(widget=forms.HiddenInput, required=False)
    
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password1 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput,
        help_text = _("Enter the same password as above, for verification."))
    
    i_am = forms.ChoiceField(error_messages={'invalid':'%(value)s is not one of the available choices.'}, 
                             choices=(("applicant","Applicant"),("company", "Company")))
    
    class Meta:
        model = User
        fields = ["username","email","i_am", "password", "password1"]

    def clean_email(self):
        if self.cleaned_data.get("username", ""):
            return self.cleaned_data.get("username", "")
    
    def clean_i_am(self):
        i_am = self.cleaned_data.get("i_am", "")
        if not i_am:
            raise forms.ValidationError(_("Please select your role"))
        return i_am
    
    def clean_password1(self):
        password1 = self.cleaned_data.get("password", "")
        password2 = self.cleaned_data["password1"]
        if password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2
    
    def clean(self):
        if not self.errors:
            self.cleaned_data['username'] = self.cleaned_data['email'].split('@')[0]
        super(RegistrationForm, self).clean()
        return self.cleaned_data
    
    def clean_username(self):
        """
        Verify that the email exists
        """
        email = self.cleaned_data.get("username", "")
        if not email:
            raise forms.ValidationError(_("Please enter an email address."))

        try:
            User.objects.get(email__iexact=email)
            raise forms.ValidationError(_("That e-mail is already used."))
        except User.DoesNotExist:
            pass
        
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get("password",""))
        
        full_name = self.cleaned_data.get("full_name","")
        full_name_to_user(user, full_name)
        
        if commit:
            user.save()
        return user
    
class PasswordChangeForm(_PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'password-change-form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            Row(HTML('<legend>Password Change</legend>')),
            Row(Column('old_password')),
            Row(Column('new_password1')),
            Row(Column('new_password2')),
			
			Row(
                Div(
                    Submit('Save', 'Save Changes', css_class='btn-primary'),
                css_class='form-actions')
            )
        )
        self.helper.add_layout(layout)

        return super(PasswordChangeForm, self).__init__(*args, **kwargs)
       
class EmailValidationForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        """
        Verify that the email exists
        """
        email = self.cleaned_data.get("email")
        if not (User.objects.filter(email=email)):# or EmailValidation.objects.filter(email=email)):
            return email

        raise forms.ValidationError(_("That e-mail is already used."))
    
class ResendEmailValidationForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        """
        Verify that the email exists
        """
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email):# or EmailValidation.objects.filter(email=email):
            return email

        raise forms.ValidationError(_("That e-mail isn't registered."))
    
