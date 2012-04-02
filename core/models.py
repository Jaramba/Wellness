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

# Create your models here.
class Person(models.Model):
	TITLES = (
		('mr','Mr.'),
		('mrs','Mrs.'),
		('miss','Miss'),
		('dr', 'Dr.'),
		('prof', 'Professor'),
	)

	title = models.CharField(max_length=20, choices=TITLES)
	middle_name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=15)

	postal_address = models.CharField(max_length=50)
	photo = models.ImageField(upload_to='photos')
	gender = models.CharField(max_length=20, choices=(('male', 'Male'),('female', 'Female')))

	country = CountryField()
	nationality = models.CharField(max_length=150, default='kenyan')

	user = models.ForeignKey(User, unique=True)
	
	date_edited = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True

User.profile = property(lambda self: Person.objects.get_or_create(user=self)[0])

