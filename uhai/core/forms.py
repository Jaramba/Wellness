from django import forms
from django.utils.crypto import get_random_string

from models import *

from crispy_forms.helper import *
from crispy_forms.layout import *

from utils import perform_raw_sql
from datetime import datetime

from django.contrib.auth.forms import UserChangeForm

class UserProfileInlineForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        
    def save(self, commit=True):
        profile = super(UserProfileInlineForm, self).save(commit=commit)
        
        if profile.user.is_healthworker:
            try:
                profile.healthworker
                profile.user.is_staff = True
                profile.user.save()
            except:
                perform_raw_sql("INSERT INTO healthprovider_healthworker (userprofile_ptr_id) VALUES (%s)", [profile.id])

        try:
            profile.patient
        except:
            perform_raw_sql(
                "INSERT INTO patient_patient (userprofile_ptr_id, patient_number) VALUES (%s, %s)", 
                [profile.id, 'PAT-%s-%s' % 
                (datetime.now().strftime('%Y'), get_random_string(4))]
            )
        
        if commit:
            profile.save()
            
        return profile

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'applicant-settings-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            HTML('<legend>Personal Profile</legend>'),
            Row(Column(Field('title', css_class='span1'))),
            Row(Column(Field('first_name', css_class='span3'))),
			Row(Column(Field('middle_name', css_class='span3'))),
			Row(Column(Field('last_name', css_class='span3'))),
			Row(Column(Field('national_id', css_class='span2'))),
            
            Row(
                Div(
                    Submit('Save', 'Save Changes', css_class='btn-primary'),
                css_class='form-actions')
            )
        )
        self.helper.add_layout(layout)
        
        return super(UserProfileForm, self).__init__(*args, **kwargs)
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = UserProfile
        fields = [
			'title','first_name','middle_name',
			'last_name','national_id',
		]
		
class LocationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'applicant-settings-form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            HTML('<legend>Location</legend>'),
            Row(Column(Field('village', css_class='span4'))),
            Row(Column(Field('county', css_class='span3'))),
			Row(Column(Field('province', css_class='span3'))),
			Row(Column(Field('country', css_class='span4'))),
            
            Row(
                Div(
                    Submit('Save', 'Save Changes', css_class='btn-primary'),
                css_class='form-actions')
            )
        )
        self.helper.add_layout(layout)
        
        return super(LocationForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = UserProfile
        fields = [
			'village',
            'province',
			'county',
			'country',
		]
		
class ContactsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'applicant-settings-form'
        self.helper.form_class = 'form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            HTML('<legend>Personal Contacts (Emergencies and Alerts)</legend>'),
            Row(Column(Field('email', css_class='span4'))),
            Row(Column(Field('postal_code', css_class='span2'))),
            Row(Column(Field('mobile_phone', css_class='span3'))),
			Row(Column(Field('home_phone', css_class='span3'))),
			Row(Column(Field('work_phone', css_class='span3'))),
                        
            Row(
                Div(
                    Submit('Save', 'Save Changes', css_class='btn-primary'),
                css_class='form-actions')
            )
        )
        self.helper.add_layout(layout)
        
        return super(ContactsForm, self).__init__(*args, **kwargs)
    
    email = forms.EmailField(help_text="The Email used to send alerts, and to communicate")
    
    class Meta:
		model = UserProfile
		fields = [
			"email", 
			"postal_code", 
			"mobile_phone",
			"home_phone",
			'work_phone'
		]
        
class RelationshipForm(forms.ModelForm):
    class Meta:
        model = Relationship

class RelationshipTypeForm(forms.ModelForm):
    class Meta:
        model = RelationshipType
