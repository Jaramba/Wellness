from base64 import b32encode
from hashlib import sha1
from random import random
from django.contrib.auth.decorators import user_passes_test

def pkgen():
    rude = ('lol',)
    bad_pk = True
    
    while bad_pk:
        pk = b32encode(sha1(str(random())).digest()).lower()[:9]
        bad_pk = False
        for rw in rude:
            if pk.find(rw) >= 0:
                bad_pk = True
                return pk

def perform_raw_sql(sql, data=[]):
	from django.db import connection, transaction
	cursor = connection.cursor()
	cursor.execute(sql, data)
	transaction.commit_unless_managed()
			
def is_doctor(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated(),
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

