from flask import Blueprint
from controller.todoController import *

todoblueprint = Blueprint('todoblueprint', __name__)

todoblueprint.route('', methods=['GET'])(fetchTodoById)
todoblueprint.route('', methods=['POST'])(insertTodo)
todoblueprint.route('', methods=['PUT'])(editTodo)
todoblueprint.route('', methods=['DELETE'])(removeTodo)