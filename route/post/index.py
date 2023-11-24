from flask import Blueprint
from controller.postController import *

postblueprint = Blueprint('postblueprint', __name__)

postblueprint.route('/', methods=['GET'])(fetchPost)
postblueprint.route('/', methods=['POST'])(addPost)