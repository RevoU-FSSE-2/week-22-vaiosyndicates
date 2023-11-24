import os
import bcrypt
import jwt
from dotenv import load_dotenv, find_dotenv
from flask import request, jsonify
from middleware.auth_middleware import *
from model.postModel import *

#load .env
load_dotenv(find_dotenv())
#get secret key
SECRET_KEY = os.environ.get("SECRET")

@user_required
async def fetchAllPost(id):
  try:
    data = await getAllPost()
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
@user_required
async def fetchPost(id):
  try:
    print(id)
    data = await getAllPostById(id)
    return jsonify({
                    'responseCode': 200,
                    'message': 'Success',
                    'data': data
                  })
  except Exception as error:
    return jsonify({
                'responseCode': 500,
                'message': 'Network Error',
                'data': error
              })

@user_required
async def addPost():
  data = request.json
  title = data.get('title')
  idUser = data.get('idUser')

  try:
    data = await createPost(title, int(idUser))
    print(data)
    return jsonify({
                    'responseCode': 200,
                    'message': 'Success',
                    'data': 'data'
                  })
  except Exception as error:
    print("An exception occurred:", type(error).__name__)
    return jsonify({
              'responseCode': 500,
              'message': 'Network Error',
              'error': error
            })