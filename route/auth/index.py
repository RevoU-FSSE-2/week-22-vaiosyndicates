from flask import Blueprint, request, jsonify
from dotenv import load_dotenv, find_dotenv
from prisma import Prisma
import asyncio
from prisma.models import User
from controller.userController import *
import os
import jwt

userblueprint = Blueprint('blueprint', __name__)

# userblueprint.route('/', methods=['GET'])(userFetch)
# userblueprint.route('/<id>', methods=['GET'])(userProfile)
userblueprint.route('/registration', methods=['POST'])(userRegistration)
userblueprint.route('/login', methods=['POST'])(userLogin)