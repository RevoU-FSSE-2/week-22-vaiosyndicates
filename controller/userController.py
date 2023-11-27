from flask import request, jsonify
from marshmallow import Schema, fields, ValidationError, validate, validates
from model.userModel import *
from middleware.auth_middleware import *
from util.index import *



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

class UserRegistrationSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=3))
    email = fields.Email(required=True)
    address = fields.String(required=False)
    password = fields.String(required=True, validate=validate.Length(min=5), load_only=True)
    role = fields.String(required=True)
async def userRegistration():
  data = request.json
  schema = UserRegistrationSchema()

  try:

    data = schema.load(data)
    pw = hash_password(data['password'])
    data['password'] = pw

    try:
      await registerUser(data['name'], data['email'], data['address'], data['password'], data['role'])
      return jsonify({
            'responseCode': 200,
            'message': 'Success'
          })

    except Exception as error:
      print(error)
      return jsonify({
            'responseCode': 500,
            'message': 'Error'
          }),500

  except ValidationError as err:
      return {"error": err.messages}, 400
  

class UserLoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=5), load_only=True)
async def userLogin():
  data = request.json
  schema = UserLoginSchema()

  try:

    data = schema.load(data)
    # print(data)
    try:
      user = await getUserByEmail(data['email'])
      if len(user) > 0:
        if(user['isApprove'] == True):
          # print(user)
          checkPW = check_password(data['password'], user['password'])
          if checkPW == False:
            return jsonify({
              'responseCode': 404,
              'message': 'Wrong password'
            }),404
          else:
            user.pop('password')
            user.pop('isApprove')
            return jsonify({
                'responseCode': 200,
                'message': 'Success',
                'data': user,
                'token': generateToken(user['id'], user['name'], user['email'], user['role'])
              }),200

        else:
          return jsonify({
            'responseCode': 404,
            'message': 'User not approved'
          }),200
      else:
        return jsonify({
            'responseCode': 404,
            'message': 'User not found'
          }),200

    except Exception as error:
      print(error)
      return jsonify({
            'responseCode': 500,
            'message': 'Error'
          }),500

  except ValidationError as err:
      return {"error": err.messages}, 400

