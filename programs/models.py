from django.db import models
from core.models import MetaData

class ProgramType(MetaData):pass
class Program(models.Model):
    '''
    This represents either an Employee Assistance Program (EAP)
    or a Patient Assistance Program (PAP). An example is a program
    to help Alcoholics 
    '''
    type = models.ForeignKey("ProgramType")
    concept_notes = models.CharField(max_length=300)
    expected_outcome_notes = models.CharField(max_length=300)

class ProgramWorkflow(models.Model):
    '''
    A program may involve certain steps that define progress
    in the program; thus we have the path and the nodes.
    The nodes are represented by the @see: ProgramWorkflowState
    and the Path represented by @see: ProgramWorkflow
    Example: An Alcoholic Program would have Workflows like:
    Family Intervention, Withdrawal...    
    '''
    program = models.ForeignKey("EnrolledProgram")
    concept_notes = models.CharField(max_length=300)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()

class ProgramWorkflowState(MetaData):
    '''
    This represents a node/milestone state of @see: ProgramWorkflow
    in the program.
    A state in the Alcoholic Program would be: Starting, Completed, or something
    '''
    workflow = models.ForeignKey("ProgramWorkflow")
    weight = models.DecimalField()
    initial = models.BooleanField(default=False)
    terminal = models.BooleanField(default=False)
    concept_notes = models.CharField(max_length=300)
        
class EnrolledProgram(models.Model):
    '''
    Patient/Employee can be enrolled in a Program to help them 
    iron out issues...
    '''
    program = models.ForeignKey("Program")
    enrollee = models.ForeignKey("core.Person")
    enroller = models.ForeignKey("core.Person")
    date_enrolled = models.DateField(auto_now=True)
    date_completed = models.DateField()
    outcome_notes = models.CharField(max_length=2000)
