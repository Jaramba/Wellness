from django import forms
from models import *
from uni_form.helper import *
from uni_form.layout import *

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
            Row(Column('medication_type')),
            Row(Column('way_taken')),
            Row(Column('strength')),
            Row(Column('min_daily_dose')),
            Row(Column('max_daily_dose')),
            Row(Column('strength')),
            Row(Column('strength_unit')),
            Row(Column('side_effects')),
            
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

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
