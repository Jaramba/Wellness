from urllib import urlopen, urlencode

BASE_URL = 'http://api.clickatell.com/http/sendmsg?%s'
USERNAME = 'samkitonyi'
PASSWORD = '26535'
API_ID = '3255886'
SENDER_ID = '254710742134' 
     
def send(recipient, message, sender=SENDER_ID):
    """Send an SMS"""
    
    vars = { 'user': USERNAME,
             'password': PASSWORD,
             'api_id': API_ID,
             'to': recipient,
             'from': sender,
             'text': message }

    url = BASE_URL % urlencode(vars)             
    return urlopen(url).read()                
