#<d7334eba615b1f843511eeae3994e5d8917947fd50b16d84b2add0ed2bb102cd>
from urllib import urlopen, urlencode
import requests, sys

BASE_URL = 'https://api.africastalking.com/version1/messaging/'
USERNAME = 'mukewa'
API_KEY = 'd7334eba615b1f843511eeae3994e5d8917947fd50b16d84b2add0ed2bb102cd'
SENDER_ID = '+254736705812' 
     
def send(recipient, message, sender=SENDER_ID):
	"""Send an SMS"""
	params = { 'username': USERNAME,
			 'to': recipient,
			 #'from': sender,
			 'message': message }
			 
	headers = {'accept': 'application/json', 'apikey':API_KEY}

	r = requests.post(BASE_URL, params=params, headers=headers, verify=False, config={'verbose': sys.stderr})
	return r.text
