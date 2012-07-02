from django import forms
from models import *
from crispy_forms.helper import *
from crispy_forms.layout import *

class MedicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'patient-insurance-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            Row(HTML('<legend>Enter Medication</legend>')),
            Row(Column('name')),
            Row(Column('medication_type'), Column('way_taken')),
            Row(Column('min_daily_dose'), Column('max_daily_dose')),
            Row(Column('strength'), Column('strength_unit')),
            Row(Column('side_effects', css_class="textarea")),
            
            Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
        )
        self.helper.add_layout(layout)

        return super(MedicationForm, self).__init__(*args, **kwargs)
    
	name = forms.CharField(required=False, help_text="Name of the insurance, if customised for the Patient.")
    
    class Meta:
        model = Medication
        exclude = ['patient']
        widgets = {
            'side_effects' : forms.Textarea
        }

class PrescriptionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'patient-insurance-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            Row(HTML('<legend>Add Prescription</legend>')),
            Row(Column('medication')),
            Row(Column('quantity'), Column('unit')),
            Row(Column('frequency'), Column('period')),
            Row(Column('reminder_type')),
            Row(Column('date_prescribed'), Column('date_started')),
            Row(Column('next_prescription_date')),
            Row(Field('reason'), css_class='textarea-column'),
            Row(Field('notes'), css_class='textarea-column'),
            
            Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
        )
        self.helper.add_layout(layout)

        return super(PrescriptionForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Prescription
        exclude = ['encounter', 'date_ended']
        widgets = {
            'reason' : forms.Textarea,
            'notes' : forms.Textarea
        }

class ImmunizationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<legend>Create Immunization</legend>')),
            Row(Column(Field('name', css_class="span4"))),
            Row(Column(Field('code'))),
            Row(Column(Field('vaccine', css_class="span3"))),
			Row(Column(Field('brand_name', css_class="span5"))),
            Row(Column(Field('duration_of_protection'))),
            Row(Column(Field('mode_of_delivery', css_class="span4"))),
            Row(Column(Field('site', css_class="span5"))),
			Row(Column(Field('practice_date'))),
            Row(Column(Field('expiry_date'))),
            Row(Column(Field('follow_up_date'))),
            Row(Field('notes'), css_class='textarea-column'),
            Row(
				Div(
					Submit('Save', 'Save Changes', css_class='btn-primary'),
				css_class='form-actions')
			)
        )
        self.helper.add_layout(self.layout)
        super(ImmunizationForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Immunization
        exclude = ['patient']
        widgets = {
            'notes': forms.Textarea
        }
