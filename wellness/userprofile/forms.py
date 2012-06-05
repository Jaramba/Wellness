from django import forms
from django.contrib.auth.forms import PasswordChangeForm as _PasswordChangeForm, AuthenticationForm as _AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from models import *
import re

from django.contrib.auth.hashers import UNUSABLE_PASSWORD, is_password_usable, get_hasher

class UserForm(forms.ModelForm):
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
    }
    username = forms.RegexField(label=_("Username"), 
        regex=r"^[\w.@+-]+$",
        help_text = _("Assigned username for login. "
                      "Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages = {
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")
        }
    )
    
    helper = FormHelper()
    helper.form_id = 'password-change-form'
    helper.form_method = 'POST'
    helper.form_action = '.'
    
    layout = Layout(
        Row(HTML('<legend>Profile</legend>')),
        Row(Column(Field('username', css_class='span6'))),
        
        Row(
            Div(
                Submit('Save', 'Save Changes', css_class='btn-primary'),
            css_class='form-actions')
        )
    )
    helper.add_layout(layout)
    
    class Meta:
        model = User
        fields = ['username']
        
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        
        if not (username == self.instance.username):
            raise forms.ValidationError(self.error_messages['duplicate_username'])
        return username
        
class AuthenticationForm(_AuthenticationForm):
    remember = forms.BooleanField(required=False)
    
class PasswordChangeForm(_PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"),
                                    widget=forms.PasswordInput, help_text='Enter your current Password')
    new_password1 = forms.CharField(label=_("New password confirmation"),
                                    widget=forms.PasswordInput, help_text='Enter your desired new Password')
    new_password2 = forms.CharField(label=_("New password confirmation"),
                                   widget=forms.PasswordInput, help_text='Repeat your new Password')
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'password-change-form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            Row(HTML('<legend>Password Change</legend>')),
            Row(Column(Field('old_password', css_class='span4'))),
            Row(Column(Field('new_password1', css_class='span4'))),
            Row(Column(Field('new_password2', css_class='span4'))),
			
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
    
