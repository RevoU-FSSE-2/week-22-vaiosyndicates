from model.todoModel import *
from flask import request, jsonify
from middleware.auth_middleware import *
from marshmallow import Schema, fields, ValidationError, validate, validates


@user_required
async def fetchTodoById(id):
  try:
    data = await getAllTodoById(id)
    return jsonify({
                    'responseCode': 200,
                    'message': 'Success',
                    'data': data
                  })
  except Exception as error:
    print(error)
    return jsonify({
                'responseCode': 500,
                'message': 'Network Error',
                'data': data
              })

class TodoAddSchema(Schema):
    
    task = fields.String(required=True, validate=validate.Length(min=3))
    time = fields.String(required=True, validate=validate.Length(min=3))

@user_required
async def insertTodo(id):
  data = request.json
  schema = TodoAddSchema()

  try:
    data = schema.load(data)

    try:
      data = schema.load(data)

      await createTodo(data['task'], data['time'], id)
      return jsonify({
            'responseCode': 200,
            'message': 'Success'
          }), 200

    except Exception as error:
      print(error)
      return jsonify({
            'responseCode': 500,
            'message': 'Error'
          }),500

  except ValidationError as err:
      return {
          "responseCode" : 400,
          "message": "Validation Error",
          "error": err.messages
        }, 400
  
class TodoUpdateSchema(Schema):
    idArticle =  fields.String(required=True, validate=validate.Length(min=1)) 
    task = fields.String(required=True, validate=validate.Length(min=3))
    time = fields.String(required=True, validate=validate.Length(min=3))
@user_required
async def editTodo(id):
  data = request.json
  schema = TodoUpdateSchema()

  try:
    data = schema.load(data)

    try:
      checkTodos = await checkTodo(int(data['idArticle']), id)

      if len(checkTodos) > 0:
          await updateTodo(int(data['idArticle']), data['task'], data['time'], id)
          return jsonify({
            'responseCode': 200,
            'message': 'Success'
          }), 200
      else:
        return jsonify({
            'responseCode': 404,
            'message': 'Todo not found'
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

class TodoDeleteSchema(Schema):
    idArticle =  fields.String(required=True, validate=validate.Length(min=1)) 

@user_required
async def removeTodo(id):
  data = request.json
  schema = TodoDeleteSchema()

  try:
    data = schema.load(data)

    try:
      checkTodos = await checkTodo(int(data['idArticle']), id)

      if len(checkTodos) > 0:
          # print(checkTodos['isDelete'])
          await deleteTodo(int(data['idArticle']), checkTodos['isDelete'])
          return jsonify({
            'responseCode': 200,
            'message': 'Success'
          }), 200
      else:
        return jsonify({
            'responseCode': 404,
            'message': 'Todo not found'
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