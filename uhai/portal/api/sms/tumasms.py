from urllib import urlopen, urlencode

BASE_URL = 'http://www.zunguka.com/kizunguzungu.sms?%s'
USERNAME = 'apopheniac'
PASSWORD = '897932'
SENDER_ID = '+254704090472'         
         
def send(recipient, message, sender=SENDER_ID):
    """Send an SMS"""
    
    vars = { 'u': USERNAME,
             'p': PASSWORD,
             'coding': 2,
             'val': 7200,
             'to': recipient,
             'from': sender,
             'msg': message }

    url = BASE_URL % urlencode(vars)             
    return urlopen(url).read()                
