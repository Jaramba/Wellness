from django import forms
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *

class EmployerCompanyForm(forms.ModelForm):
    class Meta:
        model = EmployerCompany
        
class HealthInsuranceProviderForm(forms.ModelForm):
    class Meta:
        model = HealthInsuranceProvider
        
class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
    
class PatientInsuranceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'patient-insurance-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            Row(HTML('<legend>Patient Insurance</legend>')),
            Row(Column('name')),
            Row(Column('insurance')),
            Row(Column('subscriber_policy_id')),
            Row(Column('status')),
            Row(Column('coverage_start_date')),
            Row(Column('coverage_end_date')),
            Row(Column('notes')),
            Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
        )
        self.helper.add_layout(layout)

        return super(PatientInsuranceForm, self).__init__(*args, **kwargs)
    
    name = forms.CharField(required=False, help_text="Name of the insurance, if customised for the Patient.")
    
    class Meta:
        model = PatientInsurance
        exclude = ['patient']