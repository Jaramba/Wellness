from celery.messaging import establish_connection
from kombu.compat import Publisher, Consumer

from django.contrib.auth.models import User

import requests, sys

class SMSProcessor(object):
    #Africa'sTalking SMS
    API_KEY='d7334eba615b1f843511eeae3994e5d8917947fd50b16d84b2add0ed2bb102cd'
    BASEURL='https://api.africastalking.com/version1/messaging/'

    def publish(self, message, 
        user_pk,
        exchange="sms", 
        routing_key="outgoing", 
        exchange_type="direct"):
        """Queue a message"""

        connection = establish_connection()
        publisher = Publisher(connection=connection,
                              exchange=exchange,
                              routing_key=routing_key,
                              exchange_type=exchange_type)

        publisher.send({
            'text':message,
            'recipient': User.objects.get(pk=user_pk).profile.mobile_phone
        })
        publisher.close()
        connection.close()

    def process_outgoingmessages(self, username='mukewa'):
        connection = establish_connection()
        consumer = Consumer(
            connection=connection,
            queue="sms",
            exchange="sms",
            routing_key="outgoing",
            exchange_type="direct"
        )

        try:
            for message in consumer.iterqueue():
                with transaction.commit_on_success():                     
                    requests.post(
                        BASEURL, 
                        params={ 
                            'username': username,
                            'to': message.body.get('recipient'),
                            'message': message.body.get('text')
                        },
                        headers={
                            'accept': 'application/json', 
                            'apikey':API_KEY
                        }, 
                        verify=False, 
                        config={'verbose': sys.stderr}
                    )
                    message.ack()
        finally:
            consumer.close()
            connection.close()

    def process_incomingmessages(self):
        """Process all currently gathered clicks by saving them to the
        database."""
        connection = establish_connection()
        consumer = Consumer(
            connection=connection,
            queue="sms",
            exchange="sms",
            routing_key="incoming",
            exchange_type="direct"
        )

        for message in consumer.iterqueue():
            process_text_message = message.body.get('text')
            message.ack()

        consumer.close()
        connection.close()

    def process_text_message(message):
        pass