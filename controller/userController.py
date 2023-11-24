import os
import bcrypt
import jwt
from dotenv import load_dotenv, find_dotenv
from flask import request, jsonify
from model.userModel import *
from middleware.auth_middleware import *

#load .env
load_dotenv(find_dotenv())
#get secret key
SECRET_KEY = os.environ.get("SECRET")

async def userFetch():
  try:
    data = await getUserAll()
    return jsonify({
                    'responseCode': 200,
                    'message': 'Success',
                    'data': data
                  })
  except:
    return jsonify({
                'responseCode': 500,
                'message': 'Network Error',
                'data': data
              })

async def userRegistration():
  data = request.json
  name = data.get('name')
  email = data.get('email')
  address = data.get('address')
  password = data.get('password')
  role = data.get('role')

  #hashing pw
  bytes = password.encode('utf-8')
  salt = bcrypt.gensalt()
  hash = bcrypt.hashpw(bytes, salt).decode("utf-8") 

  try:
    await registerUser(name, email, address, hash, role)
    return jsonify({
                    'responseCode': 200,
                    'message': 'Success'
                  })
  except Exception as error:
    print("An exception occurred:", type(error).__name__)
    return jsonify({
                'responseCode': 500,
                'message': 'Network Error',
                'error': error
              })
  
async def userLogin():
  data = request.json
  email = data.get('email')
  password = data.get('password')

  #encode pw
  bytes = password.encode('utf-8')

  try:
    user = await getUserByEmail(email)

    if len(user) > 0:
      user_payload = {
        "name": user['name'],
        "email": user['email'],
        "address": user['address'],
        "role": user['role']
      }
      if bcrypt.checkpw(bytes, user['password'].encode('utf-8')):
        encoded_jwt = jwt.encode({'name': user['name'], 'email': user['email'], 'role': user['role'], 'id': user['id']}, SECRET_KEY)
        return jsonify({
                        'responseCode': 200,
                        'message': 'Success',
                        'data': user_payload,
                        'token': encoded_jwt
                      })
      
      else:
        return jsonify({
                        'responseCode': 404,
                        'message': 'Wrong password'
                      }),404
    else:
      return jsonify({
                'responseCode': 404,
                'message': 'User not found'
              })
  except Exception as error:
    print("An exception occurred:", type(error).__name__)
    return jsonify({
                'responseCode': 500,
                'message': 'Network Error',
                'error': error
              })

async def userProfile(id):
  try:
      data = await getUserById(id)
      return jsonify({
                'responseCode': 200,
                'message': 'Success',
                'data': data
              })
  except Exception as error:
    print("An exception occurred:", type(error).__name__)
    return jsonify({
                'responseCode': 500,
                'message': 'Network Error',
                'error': error
              })
@user_required
async def tesUser(id):
  try:
      data = await userProfileTes(id)

      data.pop('password')
      follows = data['follows']
      data['totalFollowing'] = len(follows)

      return jsonify({
                'responseCode': 200,
                'message': 'Success',
                'data': data
              })
  except Exception as error:
    print("An exception occurred:", type(error).__name__)
    return jsonify({
                'responseCode': 500,
                'message': 'Network Error',
                'error': error
              }) 


