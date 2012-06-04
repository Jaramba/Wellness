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
            Row(HTML('<h2 class="form_title">Enter Medication</h2>')),
            Row(Column('name')),
            Row(Column('medication_type'), Column('way_taken')),
            Row(Column('min_daily_dose'), Column('max_daily_dose')),
            Row(Column('strength'), Column('strength_unit')),
            Row('side_effects'),
            
            Row(
                ButtonHolder(
                    Submit('Save', 'Save Changes'),
                )
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
            Row(HTML('<h2 class="form_title">Add Prescription</h2>')),
            Row(Column('medication')),
            Row(Column('quantity'), Column('unit')),
            Row(Column('frequency'), Column('period')),
            Row(Column('reminder_type')),
            Row(Column('date_prescribed'), Column('date_started')),
            Row(Column('next_prescription_date')),
            Row('reason'),
            Row('notes'),
            
            Row(
                ButtonHolder(
                    Submit('Save', 'Save Changes'),
                )
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
