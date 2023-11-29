from flask import request, jsonify
from middleware.auth_middleware import *
from marshmallow import Schema, fields, ValidationError, validate, validates
from model.adminModel import *
@admin_required
async def getAllUser(id):
  try:
    user = await getUsers()
    return jsonify({
                'responseCode': 200,
                'message': 'Success',
                'data': user
              }), 200
  except Exception as e:
    print(e)
    return jsonify({
                    'responseCode': 500,
                    'message': 'Network error',
                    'error': e
                  }), 500

class AdminDeleSchema(Schema):
    idUser = fields.String(required=True, validate=validate.Length(min=1))
@admin_required
async def removeUser(id):
  data = request.json
  schema = AdminApproveSchema()

  try:
    data = schema.load(data)

    try:
      checkUser = await getDetailUser(int(data['idUser']))

      if len(checkUser) > 0:
        await deleteUser(int(data['idUser']))
        return jsonify({
            'responseCode': 200,
            'message': 'Success'
          }), 200
      else:
        return jsonify({
            'responseCode': 404,
            'message': 'User not found'
          }), 404

    except Exception as error:
      print(error)
      return jsonify({
            'responseCode': 500,
            'message': error
          }),500

  except ValidationError as err:
      return {
          "responseCode" : 400,
          "message": "Validation Error",
          "error": err.messages
        }, 400

class AdminApproveSchema(Schema):
    idUser = fields.String(required=True, validate=validate.Length(min=1))
@admin_required
async def approveUser(id):
  data = request.json
  schema = AdminApproveSchema()

  try:
    data = schema.load(data)

    try:
      checkUser = await getDetailUser(int(data['idUser']))

      if len(checkUser) > 0:
        await activateUser(int(data['idUser']), checkUser['isApprove'])
        return jsonify({
            'responseCode': 200,
            'message': 'Success'
          }), 200
      else:
        return jsonify({
            'responseCode': 404,
            'message': 'User not found'
          }), 404

    except Exception as error:
      print(error)
      return jsonify({
            'responseCode': 500,
            'message': error
          }),500

  except ValidationError as err:
      return {
          "responseCode" : 400,
          "message": "Validation Error",
          "error": err.messages
        }, 400