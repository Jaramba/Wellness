from base64 import b32encode
from hashlib import sha1
from random import random

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