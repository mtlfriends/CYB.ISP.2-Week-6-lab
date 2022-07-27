import os, hashlib

def salted_password(user_password=input("Please enter your password: "), salt=os.urandom(32).hex()):
    salted_user_password = user_password + salt
    hashed_password = hashlib.sha256(salted_user_password.encode()).hexdigest()

    return hashed_password

salted_password()
 
