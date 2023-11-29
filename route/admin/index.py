from flask import Blueprint
from controller.adminController import *

adminblueprint = Blueprint('adminblueprint', __name__)

adminblueprint.route('/', methods=['GET'])(getAllUser)
adminblueprint.route('/', methods=['PUT'])(approveUser)
# adminblueprint.route('/', methods=['DELETE'])(removeTodo)