from django.db import models
from uhai.core.models import *
	
class Program(OwnerModel):
    '''
    This represents either an Employee Assistance Program (EAP)
    or a Patient Assistance Program (PAP). An example is a program
    to help Alcoholics.
    '''
    name = models.CharField(max_length=100)
    problems = models.ManyToManyField("records.Problem")
    concept_notes = models.TextField(null=True, blank=True)
    expected_outcome_notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
    	return str(self.name)

    class Meta:
        permissions = ( 
            ('view_program', 'View program'), 
        )

class EnrolledProgram(models.Model):
    '''
    Patient/Employee can be enrolled in a Program to help them
    Anyone can be enrolled to this... Even Doctors or even employees
    of Insurance companies
	Even Patients can enroll themselves to a program, for example,
	Weight loss program...
    '''
    program = models.ForeignKey("Program")
    enrollee = models.ForeignKey("patients.Patient", related_name='enrollee')
    enroller = models.ForeignKey("auth.User", related_name='enroller', verbose_name="Enrolled By")
    date_enrolled = models.DateField(auto_now=True)
    date_completed = models.DateField()
    outcome_notes = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return 'Program enrolled to: %s by %s' % (self.program, self.enrollee)
    
    class Meta:
        permissions = ( 
            ('view_enrolledprogram', 'View enrolled program'), 
        )

class ProgramWorkflow(models.Model):
    '''
    A program may involve certain steps that define progress
    in the program; thus we have the path and the nodes.
    The nodes are represented by the @see: ProgramWorkflowState
    and the Path represented by @see: ProgramWorkflow
    Example: An Alcoholic Program would have Workflows like:
    Family Intervention, Withdrawal...    
    '''
    name = models.CharField(max_length=100)
    program = models.ForeignKey("Program")
    concept_notes = models.TextField()
    continued = models.BooleanField(default=True)
    days = models.IntegerField(default=0, blank=True, null=True)
    
    def __unicode__(self):
    	return self.name
    
    class Meta:
        permissions = ( 
            ('view_enrolledprogram', 'View enrolled program'), 
        )
    
class ProgramWorkflowState(models.Model):
    '''
    This represents a node/milestone state of @see: PrenrolleeogramWorkflow
    in the program.
    A state in the Alcoholic Program would be: Starting, Completed, or something
    '''
    name = models.CharField(max_length=120)
    program_workflow = models.ForeignKey("ProgramWorkflow")
    weight = models.IntegerField(default=0)
    initial = models.BooleanField(default=False)
    terminal = models.BooleanField(default=False)
    concept_notes = models.TextField()
    
    def __unicode__(self):
    	return 'Node: %s %s' % (self.name, self.program_workflow)
    
    class Meta:
        permissions = ( 
            ('view_programworkflowstate', 'View program workflow state'), 
        )

class Questionnaire(models.Model):
	name = models.CharField(max_length=255)
	intro = models.CharField('Introduction', max_length=20, null=True, blank=False)
	detail = models.CharField('Details', max_length=100, null=True, blank=False)
	notes = models.TextField(max_length=2000, null=True, blank=False, 
			help_text=r"Use simple HTML tags &lt;p&gt;&lt;/p&gt; for paragraphs, "
					"&lt;blockquote&gt;&lt;/blockquote&gt; for lists "
					"and &lt;li&gt;&lt;ul&gt;&lt;/ul&gt;&lt;/li&gt; to enclose list of things")
	program = models.ForeignKey('programs.Program')
	date_created = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
	    permissions = ( 
	        ('view_questionnaire', 'View questionnaire'), 
	    )

class QuestionSetManager(models.Manager):
	def get_query_set(self):
		qs = super(QuestionSetManager, self).get_query_set()
		return qs.filter(answerable_by='patient')
		
class QuestionSet(models.Model):
	ANSWERABLE_BY = [
		('patient', 'Patient'),
		('doctor', 'Doctor'),
		('employer', 'Employer'),
	]
	label = models.CharField(max_length=255, blank=True, null=True)
	answerable_by = models.CharField(max_length=50, choices=ANSWERABLE_BY, null=True, blank=False, help_text='Questions in this section are answerable by who?')
	questionnaire = models.ForeignKey(Questionnaire, blank=True)
	date_created = models.DateTimeField(auto_now=True)
		
	objects = models.Manager()
	pq_objects = QuestionSetManager()	
		
	def __unicode__(self):
		return '%s from %s' % (self.label, self.questionnaire)
	
	@property
	def length(self): 
		return self.question_set.count()
		
	class Meta:
	    permissions = ( 
	        ('view_questionset', 'View questionset'), 
	    )
	
class Question(models.Model):
	TYPES=[
		('yes-no', 'Yes/No'),
		('number', 'Number'),
		('text', 'Text'),
		('datetime', 'Date/Time'),
		('choice', 'Choice')
	]
	text = models.CharField(max_length=255)
	questionset = models.ForeignKey(QuestionSet, blank=True)
	type = models.CharField(max_length=255, choices=TYPES)
	choices = models.CharField(max_length=255, 
		null=True, blank=True, 
		help_text='If choices, type here a set of comma-separated choices'
	)
	choice_explicit = models.BooleanField(default=False, help_text='If choices, can you choose more than one choices?')

	def __unicode__(self):
		return self.text
		
	@property
	def choices_list(self):
		return [c.strip() for c in self.choices.split(',')]

	class Meta:
		permissions = ( 
			('view_question', 'View question'), 
		)

class PatientQuestionnaire(models.Model):
	"""
	Represents the event where a patient answered a questionnaire
	"""
	PERIODS = [
		('every-hour', 'Hourly'),
		('twice-a-day', 'Twice daily'),
		('thrice-a-day', 'Thrice daily'),
		('four-times-a-day', 'Four times daily'),
		('five-times-a-day', 'Five times daily'),
		('six-times-a-day', 'Six times daily'),
		('seven-times-a-day', 'Seven times daily'),
		('eight-times-a-day', 'Eight times daily'),
		('daily', 'Daily'),
		('weekly', 'Weekly'),
		('monthly', 'Monthly'),
		('three-months', 'Three months'),
		('six-months', 'Six months'),
		('nine-months', 'Nine months'),
		('yearly', 'Yearly')
	]
	questionnaire = models.ForeignKey('Questionnaire')
	patient = models.ForeignKey('patients.Patient')
	frequency = models.CharField(max_length=25, choices=PERIODS, help_text='Frequency the patient should fill the questionnaire')
	completed = models.BooleanField(default=False)
	updated_at = models.DateTimeField(auto_now_add=True)
	
class Response(models.Model):
	"""
	Records a student's response to a given question at a 
	particular sitting
	Can be filled by Doctor... or another person
	"""
	patient 	= models.ForeignKey('patients.Patient')
	answered_by	= models.ForeignKey('auth.User')
	question 	= models.ForeignKey(Question)
	value 		= models.CharField(max_length=255)
	response_date 	= models.DateTimeField("Date updated", default=datetime.now)

	def __unicode__(self):
		return self.question.text
	
	class Meta:
	    permissions = ( 
	        ('view_response', 'View response'), 
	    )