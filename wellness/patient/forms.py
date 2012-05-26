from django import forms
from models import *

class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'patient-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            Row(Column('title')),
            Row(Column('first_name'),Column('middle_name'),Column('last_name')),
            Row(Column('email')),
            Row(Column('mobile_phone'),Column('mobile_phone'),Column('work_phone')),
            Row(Column('postal_address')),
            Row(Column('gender')),
            Row(Column('country'), Column('nationality')),
            Row(Column('blood_group')),
            Row(Column('weight'), Column('height')),
            Row(Column('employer')),
            Row(Column('doctor')),
            Row(Column('disabilities')),
            Row(
                ButtonHolder(
                    Submit('Save', 'Save Changes'),
                )
            )
        )
        self.helper.add_layout(layout)
        
        return super(HealthWorkerForm, self).__init__(*args, **kwargs)
    
    gender = forms.ChoiceField(
        choices=(('','Select your gender'),('male','Male'),('female','Female')), 
        help_text="Whats your gender?"
    )
    birthday = forms.DateField(input_formats=['%d/%m/%Y','%Y-%m-%d'], required=False)
    
    class Meta:
        model = Patient
