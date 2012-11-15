import requests

from django.conf import settings
from django.db import transaction
from django.utils.timezone import now

from celery.messaging import establish_connection
from kombu.compat import Publisher, Consumer

class ReminderProcessor(object):
	def __init__(self, *args, **kwargs):
		pass

	def prepare_publisher(self, routing_key='', 
		exchange='', exchange_type="direct"):
		connection = establish_connection()
	    publisher = Publisher(connection=connection,
	                          exchange=exchange,
	                          routing_key=routing_key,
	                          exchange_type=exchange_type)
	    return publisher

	def due_prescriptions(self):
		prescriptions = Prescription.objects.filter(
			dose_cleared__isnotnull=True,
			date_dose_cleared__lt=now()
		)

		publisher = prepare_publisher()

		for prescription in  prescriptions:
			publisher.send()


	def enrolledprograms(self):
		pass

	def vitals(self):
		pass	

	def questionnaires(self):
		pass