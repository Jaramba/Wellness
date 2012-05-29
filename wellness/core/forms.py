from django import forms
from django.utils.crypto import get_random_string

from models import *

from uni_form.helper import *
from uni_form.layout import *

from utils import perform_raw_sql
from datetime import datetime

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
            HTML('<h2 class="form_title">Personal Profile</h2>'),
            Row(Column('title')),
            Row(Column('first_name', css_class='names'), Column('middle_name', css_class='names'), Column('last_name', css_class='names'),), 
            Row(Column('email')),
            Row(Column('postal_code'), Column('village'),),
            Row(Column('province'), Column('home_address')),
            Row(Column('county'), Column('country')),
            Row(Column('mobile_phone'), Column('home_phone'), Column('work_phone')),
            Row(Column('photo')),
            
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
    
    class Meta:
        model = UserProfile
        exclude = ["user", "relationship", "tags", "longitude","latitude",]
        widgets = {
            'picture':forms.HiddenInput
        }

class RelationshipForm(forms.ModelForm):
    class Meta:
        model = Relationship

class RelationshipTypeForm(forms.ModelForm):
    class Meta:
        model = RelationshipType
