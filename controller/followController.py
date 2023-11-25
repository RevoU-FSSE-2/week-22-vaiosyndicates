import os
import bcrypt
import jwt
from dotenv import load_dotenv, find_dotenv
from flask import request, jsonify
from middleware.auth_middleware import *
from model.followModel import *

#load .env
load_dotenv(find_dotenv())
#get secret key
SECRET_KEY = os.environ.get("SECRET")

@user_required
async def createFollower(id):
  data = request.json
  idOther = data.get('idOther')

  if int(idOther) == id:
    return jsonify({
                    'responseCode': 404,
                    'message': 'Cannot follow same user',
                  }),404


  try:
    # checkOther = await checkIsIDExist(id, int(idOther))
    # return jsonify({
    #                 'responseCode': 404,
    #                 'message': 'Already followed',
    #               }),404    
    # print(type(checkOther))
    # if checkOther:
    #   return jsonify({
    #             'responseCode': 404,
    #             'message': 'Already followed',
    #           }),404
    # else:

      data = await addFollower(id, int(idOther))
      return jsonify({
                    'responseCode': 200,
                    'message': 'Success',
                  }),200
    # else:

    # else:
    # data = await addFollower(id, int(idOther))
    # return jsonify({
    #                 'responseCode': 200,
    #                 'message': 'Success',
    #               }),200
    #   data = await addFollower(id, int(idOther))
    #   return jsonify({
    #                   'responseCode': 200,
    #                   'message': 'Success',
    #                 }),200
  
  except Exception as error:
    # print("An exception occurred:", type(error).__name__)
    print(error)
    return jsonify({
              'responseCode': 500,
              'message': 'Network Error',
              'error': error
            }),500

@user_required
async def removeFollower(id):
  data = request.json
  idOther = data.get('idOther')

  try:
    checkOther = await checkIsIDExist(id, int(idOther))
    if checkOther:
      return jsonify({
                      'responseCode': 404,
                      'message': 'Already Deleted',
                    }),404
    
    data = await deleteFollower(id, int(idOther))
    return jsonify({
                    'responseCode': 200,
                    'message': 'Success',
                  }),200
  except Exception as error:
    print("An exception occurred:", type(error).__name__)
    return jsonify({
              'responseCode': 500,
              'message': 'Network Error',
              'error': error
            }),500