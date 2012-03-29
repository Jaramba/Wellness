from django import forms
from django.contrib.auth.forms import PasswordChangeForm as _PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from recruit.util import full_name_to_user
from uni_form.helper import FormHelper
from uni_form.layout import *
from models import *
import re

class CompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'password-change-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            Row(HTML('<h2 class="form_title">Company Profile: {{ company.name }}</h2>')),
            Row(Column('name')),
            Row(Column('contact_person'), Column('phone')),
            Row(Column('country'), Column('city')), 
            Row(Column('postal_address')),
            Row(Column('industries')),
            Row(Column('about')),
            Row(Column('logo')),
            Row(
                ButtonHolder(
                    Submit('Save', 'Save Changes'),
                )
            )
        )
        self.helper.add_layout(layout)

        return super(CompanyForm, self).__init__(*args, **kwargs)

    about = forms.CharField(
        label="About",
        required=False,
        widget=forms.Textarea,
        help_text="A short descriptive background of the company."
    )

    class Meta:
        model = Company
        exclude = ["slug"]

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
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            Row(HTML('<h2 class="form_title">Password Change</h2>')),
            Row(Column('old_password')),
            Row(Column('new_password1')),
            Row(Column('new_password2')),
            Row(
                ButtonHolder(
                    Submit('Save', 'Save Changes'),
                )
            )
        )
        self.helper.add_layout(layout)

        return super(PasswordChangeForm, self).__init__(*args, **kwargs)

    
class RecruiterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'recruiter-settings-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            Row(HTML('<h2 class="form_title">Personal Profile</h2>')),
            Row(Column('first_name'),Column('last_name')),
            Row(Column('email')),
            Row(Column('phone')),
            Row(Column('country'), Column('city')), 
            Row(Column('postal_address')),
            Row(
                ButtonHolder(
                    Submit('Save', 'Save Changes'),
                )
            )
        )
        self.helper.add_layout(layout)
        
        return super(RecruiterForm, self).__init__(*args, **kwargs)
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField(label="Home city/town", help_text="What is your home city/town?")
    
    class Meta:
        model = UserProfile
        fields=['first_name','first_name','email','country','city','postal_address','phone']
        exclude = ["default_dashboard"]

class ApplicantBase(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    birthday = forms.DateField(input_formats=['%d/%m/%Y','%Y-%m-%d'], widget=forms.DateInput(format='%d/%m/%Y'), required=False, help_text="When were you born?")

    class Meta:
        model = UserProfile
        fields=[
            'first_name','last_name','email',
            'birthday','gender',
            'country','city',
            'postal_address','phone',
            'picture'
        ]
        widgets = {
            'picture':forms.HiddenInput
        }
        
class CvApplicantForm(ApplicantBase):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'applicant-settings-form'
        self.helper.form_class = 'cv_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        layout = Layout(
            Row(Column('first_name')), 
            Row(Column('last_name')),
            Row(Column('email')),
            Row(Column('phone')),
            Row(Column('birthday')), 
            Row(Column('gender')), 
            Row(Column('country')), 
            Row(Column('city')),
            Row(Column('postal_address')),
            Row(
                ButtonHolder(
                    Submit('Save', 'Save Changes'),
                )
            )
        )
        self.helper.add_layout(layout)
        return super(CvApplicantForm, self).__init__(*args, **kwargs)
    class Meta:
        model = UserProfile
        fields=[
            'first_name','last_name','email',
            'birthday','gender',
            'country','city',
            'postal_address','phone',
        ]

class ApplicantForm(ApplicantBase):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'applicant-settings-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            HTML('<h2 class="form_title">Personal Profile</h2>'),
            Row(Column('first_name'), Column('last_name')),
            Row(Column('email'),),
            Row(Column('phone')),
            Row(Column('birthday'), Column('gender')), 
            Row(Column('country'), Column('city')),
            Row(Column('postal_address')),
            Row(Column('picture')),
            Row(
                ButtonHolder(
                    Submit('Save', 'Save Changes'),
                )
            )
        )
        self.helper.add_layout(layout)
        
        return super(ApplicantForm, self).__init__(*args, **kwargs)
    
class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'applicant-settings-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            HTML('<h2 class="form_title">Personal Profile</h2>'),
            Row(
                Column(
                       HTML("""
                           <label style="margin-left:10px;">Profile Picture</label>
                           <div id="settings-image">
                                <div id="settings-image-holder">
                                    <img id="setting-profile-pic" src="{{ MEDIA_URL }}{{ profile.picture|default:'profilepics/default_avatar.png' }}"/>
                                </div>
                                <div id="image-upload-button" style="float: left;width: 50%;"></div>
                           </div>
                       """),
                       'picture'
                   ),
                Column('description')
            ),
            Row(Column('first_name'), Column('last_name'),), 
            Row(Column('email'),Column('phone')),
            Row(Column('gender'), Column('birthday'),),
            Row(Column('country'), Column('city')),
            Row(Column('postal_address'), Column('education')),
            
            Row(
                ButtonHolder(
                    Submit('Save', 'Save Changes'),
                )
            )
        )
        self.helper.add_layout(layout)
        
        return super(UserProfileForm, self).__init__(*args, **kwargs)
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(help_text="The Email used to send alerts")
    description = forms.CharField(label="Bio", widget=forms.Textarea, max_length=200, help_text="A brief about myself")
    gender = forms.ChoiceField(
        choices=(('','Select your gender'),('male','Male'),('female','Female')), 
        help_text="Whats your gender?"
    )
    education = forms.ChoiceField(
        choices=(
            ('school-of-life','School of life'),
            ('high-school','High School'),
            ('certificate','Certificate'),
            ('diploma', 'Diploma'),
            ('graduate','Graduate'),
            ('post-graduate','Post Graduate'),
            ('phd','PhD'),
            ('professor','Professor'),
        ),
        help_text="Select your level of Education"
    )
    birthday = forms.DateField(input_formats=['%d/%m/%Y','%Y-%m-%d'], required=False)
    
    class Meta:
        model = UserProfile
        exclude = ["user", "is_active_profile", "tags", "companies","default_dashboard"]
        widgets = {
            'picture':forms.HiddenInput
        }
        
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
    
    
