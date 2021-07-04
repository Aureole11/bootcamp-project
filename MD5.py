import hashlib
import os

print(hashlib.algorithms_available)

salt = os.urandom(32)
s = input("enter any string: ")

print(hashlib.md5(s.encode('utf-8')).hexdigest())
print(hashlib.pbkdf2_hmac('md5',s.encode('utf-8'),salt,5).hex())

print(hashlib.sha3_224(s.encode('utf-8')).hexdigest())
print(hashlib.pbkdf2_hmac('sha3_224',s.encode('utf-8'),salt,5).hex())

print(hashlib.sha256(s.encode('utf-8')).hexdigest())
print(hashlib.pbkdf2_hmac('sha256',s.encode('utf-8'),salt,5).hex())

input('press enter to exit...')

