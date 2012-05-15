from django import forms
from models import UserProfile
from uni_form.helper import *
from uni_form.layout import *

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
            Row(Column('first_name'), Column('middle_name'),), 
            Row(Column('last_name'), Column('email')),
            Row(Column('gender'), Column('birthday'),),
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
    gender = forms.ChoiceField(
        choices=(('','Select your gender'),('male','Male'),('female','Female')), 
        help_text="Whats your gender?"
    )
    birthday = forms.DateField(input_formats=['%d/%m/%Y','%Y-%m-%d'], required=False)
    
    class Meta:
        model = UserProfile
        exclude = ["user", "relationship", "tags", "longitude","latitude",]
        widgets = {
            'picture':forms.HiddenInput
        }
