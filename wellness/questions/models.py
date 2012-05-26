from django.db import models
from django.contrib.auth.models import User
from wellness.core.models import MetaData

class ProgramQuestionnaire(models.Model):
	name = models.CharField(max_length=255)
	program = models.ForeignKey('programs.Program')
	start_date = models.DateTimeField(null=True, blank=True)
	finish_date = models.DateTimeField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now=True)

	@property
	def length(self): 
		return self.question_set.count()

	def __unicode__(self):
		return self.name

class QuestionSet(models.Model):
	label = models.CharField(max_length=255, blank=True, null=True)
	questionnaire = models.ForeignKey(ProgramQuestionnaire, blank=True)
	date_created = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.label
	
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
	type = models.CharField(max_length=255, null=True, blank=True, choices=TYPES)
	choices = models.CharField(max_length=255, 
		null=True, blank=True, 
		help_text='If choices, type here a set of comma-separated choices'
	)

	def __unicode__(self):
		return self.text

class PatientProgramQuestionnaire(models.Model):
	"""
	Represents the event where a patient answered a questionnaire
	"""
	questionnaire = models.ForeignKey('ProgramQuestionnaire')
	enrolled_program = models.ForeignKey('programs.EnrolledProgram')
	completed = models.BooleanField(default=False)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return '%s enrolled for %s' % (self.questionnaire, self.enrolled_program)

class Response(models.Model):
	"""
	Records a student's response to a given question at a 
	particular sitting
	"""
	patient_program_questionnaire = models.ForeignKey(PatientProgramQuestionnaire)
	question = models.ForeignKey(Question)
	value = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.question.text
		