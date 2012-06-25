from django.db import models
from django.contrib.auth.models import User
from uhai.core.models import MetaData

class ProgramQuestionnaire(models.Model):
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
	        ('view_programquestionnaire', 'View program questionnaire'), 
	    )

class PatientQuestionnaireManager(models.Manager):
	def get_query_set(self):
		qs = super(PatientQuestionnaireManager, self).get_query_set()
		return qs.filter(answerable_by='patient')
		
class QuestionSet(models.Model):
	ANSWERABLE_BY = [
		('patient', 'Patient'),
		('doctor', 'Doctor'),
		('employer', 'Employer'),
	]
	label = models.CharField(max_length=255, blank=True, null=True)
	answerable_by = models.CharField(max_length=50, choices=ANSWERABLE_BY, null=True, blank=False, help_text='Questions in this section are answerable by who?')
	questionnaire = models.ForeignKey(ProgramQuestionnaire, blank=True)
	date_created = models.DateTimeField(auto_now=True)
		
	objects = models.Manager()
	pq_objects = PatientQuestionnaireManager()	
		
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

class PatientProgramQuestionnaire(models.Model):
	"""
	Represents the event where a patient answered a questionnaire
	"""
	questionnaire = models.ForeignKey('ProgramQuestionnaire')
	enrolled_program = models.ForeignKey('programs.EnrolledProgram')
	completed = models.BooleanField(default=False)
	updated_at = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return '%s enrolled for %s' % (self.questionnaire, self.enrolled_program)
	
	class Meta:
	    permissions = ( 
	        ('view_patientprogramquestionnaire', 'View patient program questionnaire'), 
	    )

class Response(models.Model):
	"""
	Records a student's response to a given question at a 
	particular sitting
	"""
	patient = models.ForeignKey('patient.Patient', related_name='reponse_patient')
	answer_by = models.ForeignKey('userprofile.UserProfile')
	question = models.ForeignKey(Question)
	value = models.CharField(max_length=255)

	def __unicode__(self):
		return self.question.text
	
	class Meta:
	    permissions = ( 
	        ('view_response', 'View response'), 
	    )
		