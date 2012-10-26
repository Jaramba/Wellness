from django import forms
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *

class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'patient-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
			HTML('<legend>Medical Profile</legend>'),
            Row(Column(Field('blood_group', css_class='span1'))),
			Row(Column(Field('gender', css_class='span2'))),
			Row(Column(Field('date_of_birth', css_class='span3'))),
			Row(Column(Field('weight', css_class='span4'))),
			Row(Column(Field('height', css_class='span4'))),
            Row(
                Div(
                    Submit('Save', 'Save Changes', css_class='btn-primary'),
                css_class='form-actions')
            )
        )
        self.helper.add_layout(layout)
        
        return super(PatientForm, self).__init__(*args, **kwargs)
    
    gender = forms.ChoiceField(
        choices=(('','Select your gender'),('male','Male'),('female','Female')), 
        help_text="Whats your gender?"
    )
    date_of_birth = forms.DateField(
		input_formats=['%d/%m/%Y','%Y-%m-%d'], required=False, 
		help_text='The Patient\'s indicated date of birth'
	)
    
    class Meta:
		model = Patient
		exclude = [
			'user', 'employer', 'providers', 'insurance'
		]


class PatientProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'patient-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
			HTML('<legend>Medical Profile</legend>'),
            Row(Column(Field('blood_group', css_class='span1'))),
			Row(Column(Field('gender', css_class='span2'))),
			Row(Column(Field('date_of_birth', css_class='span3'))),
			Row(Column(Field('weight', css_class='span4'))),
			Row(Column(Field('height', css_class='span4'))),
            Row(
                Div(
                    Submit('Save', 'Save Changes', css_class='btn-primary'),
                css_class='form-actions')
            )
        )
        self.helper.add_layout(layout)
        
        return super(PatientProfileForm, self).__init__(*args, **kwargs)
    
    gender = forms.ChoiceField(
        choices=(('','Select your gender'),('male','Male'),('female','Female')), 
        help_text="Whats your gender?"
    )
    date_of_birth = forms.DateField(
		input_formats=['%d/%m/%Y','%Y-%m-%d'], required=False, 
		help_text='The Patient\'s indicated date of birth'
	)
    
    class Meta:
		model = Patient
		exclude = [
			'user', 'employer', 'providers', 'insurance'
		]
