import requests

from django.conf import settings
from django.db import transaction
from django.utils.timezone import now

from celery.messaging import establish_connection
from kombu.compat import Publisher, Consumer

class ReminderProcessor(object):
	def __init__(self, *args, **kwargs):
		pass

	def due_prescriptions(self):
		prescriptions = Prescription.objects.filter(
			dose_cleared__isnotnull=True,
			date_dose_cleared__lt=now()
		)

		connection = establish_connection()
	    publisher = Publisher(connection=connection,
	                          exchange='reminders',
	                          routing_key='prescriptions',
	                          exchange_type='direct')
		for prescription in prescriptions:			
			publisher.send({
				'text':'Please remember that your have some prescriptions for {0} due in {1} day{2}.',
				'user':
			})

	def enrolledprograms(self):
		pass

	def vitals(self):
		pass	

	def questionnaires(self):
		pass