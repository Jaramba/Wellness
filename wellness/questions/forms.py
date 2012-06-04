from django import forms
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *

class PatientProgramQuestionnaireForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'patient-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
        
        layout = Layout(
            Row(Column('questionnaire')),            
            Row(Column('enrolled_program')),
            Row(Column('completed')),
            Row(
                ButtonHolder(
                    Submit('Save', 'Save Changes'),
                )
            )
        )
        self.helper.add_layout(layout)
        
        return super(PatientProgramQuestionnaireForm, self).__init__(*args, **kwargs)
    
    class Meta:
		model = PatientProgramQuestionnaire
		exclude = [
		]
