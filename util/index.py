import bcrypt
import jwt
import os
from dotenv import load_dotenv, find_dotenv

#load .env
load_dotenv(find_dotenv())
#get secret key
SECRET_KEY = os.environ.get("SECRET")

def hash_password(password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode("utf-8")

def check_password(curPW, password):
    bytes = curPW.encode('utf-8')

    if bcrypt.checkpw(bytes, password.encode('utf-8')):
        return True
    else:
        return False

def generateToken(id, name, email, role):
    encoded_jwt = jwt.encode({'id': id, 'name': name, 'email': email, 'role': role}, SECRET_KEY, algorithm='HS256')
    return encoded_jwt
    