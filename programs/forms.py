from django import forms
from models import *
from uni_form.helper import FormHelper
from uni_form.layout import *

class ProgramTypeForm(forms.ModelForm):
    class Meta:
        model = ProgramType
        
class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
 
class ProgramWorkflowForm(forms.ModelForm):
    class Meta:
        model = ProgramWorkflow

class ProgramWorkflowStateForm(forms.ModelForm):
    class Meta:
        model = ProgramWorkflowState

class EnrolledProgramForm(forms.ModelForm):
    class Meta:
        model = EnrolledProgram
