from django.db import models
from django.auth.contrib.models import User

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
	phone_number = models.RegexField()

	postal_address = models.CharField(max_length=50)
	photo = models.ImageField()
	gender = models.CharField(max_length=20, choices=(('male', 'Male'),('female', 'Female')))
	nationality = models.CharField()

	user = models.ForeignKey(unique=True)
	
	date_edited = models.DatetimeField(auto_now=True)
	date_created = models.DatetimeField(auto_now=True)
	
	class Meta:
		abstract = True
	
User.profile = lambda self:self.__class__.objects.get_or_create(user=self.user)[0]

