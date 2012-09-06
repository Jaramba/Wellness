from django import forms
from models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
        
class ProgramForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<h2 class="form_title">Create Immunization</h2>'), css_class="form_title_div"),
            Row(Column('name')),
            Row(Column('type')),
            Row(Column('is_public')),
            Row(Column('problem')),
            Row('concept_notes'),
            Row('expected_outcome_notes'),
            Row(
                Column(
                    Submit('Save', 'Save Changes'),
                )
            )
        )
        self.helper.add_layout(self.layout)
        super(ProgramForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Program
        exclude = ['program_owner']
        widgets = {
            'concept_notes': forms.Textarea,
            'expected_outcome_notes': forms.Textarea
        }
 
class ProgramWorkflowForm(forms.ModelForm):
    class Meta:
        model = ProgramWorkflow

class ProgramWorkflowStateForm(forms.ModelForm):
    class Meta:
        model = ProgramWorkflowState

class EnrolledProgramForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'problem-form'
        self.helper.form_class = 'general_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = '#'
        
        self.layout = Layout(
            Div(HTML('<h2 class="form_title">Create Immunization</h2>'), css_class="form_title_div"),
            Row(Column('program')),
            Row(Column('enroller')),
            Row(Column('enrollee')),
            Row(Column('date_completed')),
            Row('outcome_notes'),
            Row(
                Column(
                    Submit('Save', 'Save Changes'),
                )
            )
        )
        self.helper.add_layout(self.layout)
        super(EnrolledProgramForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = EnrolledProgram
        widgets = {
            'outcome_notes': forms.Textarea
        }
		