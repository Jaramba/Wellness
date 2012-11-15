from urllib import urlopen, urlencode
import requests, sys

from celery import task
from django.db import transaction

@task
def africastalking(recipient, message_pk, sender='+254736705812',
	base_url = 'https://api.africastalking.com/version1/messaging/'
	username = 'mukewa'
	api_key = 'd7334eba615b1f843511eeae3994e5d8917947fd50b16d84b2add0ed2bb102cd'
	):
	"""Send an SMS vis africastalking"""
    for message in SmsMessageOutbox.objects.filter(timestamp__isnull=True):
		with transaction.commit_on_success():
			message.timestamp = datetime.now()
					 
			message.gateway_response = requests.post(
				base_url, 
				params={ 
					'username': username,
					'to': message.destination,
					#'from': sender,
					'message': message.text 
				},
				headers={
					'accept': 'application/json', 
					'apikey':api_key
				}, 
				verify=False, 
				config={'verbose': sys.stderr}
			).text
			message.save()

@task
def clickatell(recipient, 
	message, 
	base_url = 'http://api.clickatell.com/http/sendmsg?%s',
	username = 'samkitonyi',
	password = '26535',
	api_id = '3255886',
	sender = '254710742134'
	):
    """Send an SMS via clickatell"""
    
    vars = { 'user': username,
             'password': password,
             'api_id': api_id,
             'to': recipient,
             'from': sender,
             'text': message }

    r = requests.post(base_url, params=params, verify=False, config={'verbose': sys.stderr})
	return r.text

@task    
def tumasms(recipient, message, 
	base_url = 'http://www.zunguka.com/kizunguzungu.sms?%s',
	username = 'apopheniac',
	password = '897932',
	sender = '+254704090472'):
	"""Send an SMS via tumasms"""

	vars = { 'u': username,
	         'p': password,
	         'coding': 2,
	         'val': 7200,
	         'to': recipient,
	         'from': sender,
	         'msg': message }

	r = requests.post(base_url, params=params, verify=False, config={'verbose': sys.stderr})
	return r.text
