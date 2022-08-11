import os, hashlib

def salted_password(user_password=input("Please enter your password: "), salt=os.urandom(32).hex()):
    added_salt = user_password + salt
    
    # print(added_salt)
    # print(hashlib.sha256(added_salt.encode()).hexdigest())
    
    return hashlib.sha256(added_salt.encode()).hexdigest()
    
salted_password()
 
