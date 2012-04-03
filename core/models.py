from django.db import models
from django.contrib.auth.models import User

from fields import  *

class Reminder(models.Model):
	REPEATS = []
	
	start = models.DateTimeField()
	duration = models.CharField(max_length=20)
	all_day = models.BooleanField(default=False)
	occurence_pattern = models.CharField(max_length=100)

class Record(models.Model):
	name = models.CharField(max_length=30)
	user = models.ForeignKey("auth.User")
	attachments = models.ManyToManyField("Attachment")
	notes = models.CharField(max_length=2000)
	
	class Meta:
		abstract=True
		
class Attachment(models.Model):
	name = models.CharField(max_length=120)
	file = models.FileField(upload_to="attachments")
	date_of_upload = models.DateTimeField(auto_now_add=True)

#Lets get this clear: EVERYONE is a Patient
class Person(models.Model):
	TITLES = (
		('mr','Mr.'),
		('mrs','Mrs.'),
		('miss','Miss'),
		('dr', 'Dr.'),
		('prof', 'Professor'),
	)
	GENDER = (
		('male', 'Male'),
		('female', 'Female')
	)

	title = models.CharField(max_length=20, choices=TITLES)
	middle_name = models.CharField(max_length=50)
	
	mobile_phone = models.CharField(max_length=50)
	home_phone = models.CharField(max_length=50)
	work_phone = models.CharField(max_length=50)

	postal_address = models.CharField(max_length=50)
	photo = models.ImageField(upload_to='photos')
	gender = models.CharField(max_length=20, choices=GENDER)

	country = CountryField()
	nationality = models.CharField(max_length=150, default='kenyan')
	
	employer = models.ForeignKey('insuranceprovider.EmployerCompany')
	
	date_edited = models.DateTimeField(auto_now_add=True)
	date_created = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True

@property
def is_healthprovider(self):
	return self.groups.filter(name='Health workers').count()
User.is_healthprovider = is_healthprovider

@property
def is_employer(self):
	return self.groups.filter(name='Employers').count()
User.is_employer = is_employer

@property
def is_insuranceprovider(self):
	return self.groups.filter(name='Insurance agents').count()
User.is_insuranceprovider = is_insuranceprovider
