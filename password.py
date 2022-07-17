import os, hashlib

def salted_password(user_password=input("Please enter your password: "), salt=os.urandom(32).hex()):
    return hashlib.sha256(user_password.encode() + salt.encode()).hexdigest()

salted_password()
 
