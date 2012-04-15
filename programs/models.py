from django.db import models
from core.models import MetaData

class ProgramType(MetaData):
    '''
    Meta-definer of the program; The type of program
    '''
    pass

class Program(models.Model):
    '''
    This represents either an Employee Assistance Program (EAP)
    or a Patient Assistance Program (PAP). An example is a program
    to help Alcoholics 
    '''
    type = models.ForeignKey("ProgramType")
    concept_notes = models.CharField(max_length=500)
    expected_outcome_notes = models.CharField(max_length=500)
    
    def __unicode__(self):
        return str(self.type) 

class ProgramWorkflow(models.Model):
    '''
    A program may involve certain steps that define progress
    in the program; thus we have the path and the nodes.
    The nodes are represented by the @see: ProgramWorkflowState
    and the Path represented by @see: ProgramWorkflow
    Example: An Alcoholic Program would have Workflows like:
    Family Intervention, Withdrawal...    
    '''
    enrolled_program = models.ForeignKey("EnrolledProgram")
    concept_notes = models.CharField(max_length=500)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()

class ProgramWorkflowState(MetaData):
    '''
    This represents a node/milestone state of @see: PrenrolleeogramWorkflow
    in the program.
    A state in the Alcoholic Program would be: Starting, Completed, or something
    '''
    program_workflow = models.ForeignKey("ProgramWorkflow")
    weight = models.CharField(max_length=5)
    initial = models.BooleanField(default=False)
    terminal = models.BooleanField(default=False)
    concept_notes = models.CharField(max_length=500)
        
class EnrolledProgram(models.Model):
    '''
    Patient/Employee can be enrolled in a Program to help them
    Anyone can be enrolled to this... Even Doctors or even employees
    of Insurance companies
    '''
    program = models.ForeignKey("Program")
    enrollee = models.ForeignKey("core.Person", related_name='enrollee')
    enroller = models.ForeignKey("core.Person", related_name='enroller')
    date_enrolled = models.DateField(auto_now=True)
    date_completed = models.DateField()
    outcome_notes = models.CharField(max_length=2000, null=True, blank=True)
    
    def __unicode__(self):
        return str(self.enrollee) + ' enrolled to ' + str(self.program)  
