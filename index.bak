from flask import Flask
from dotenv import load_dotenv, find_dotenv
from flask_cors import CORS
from route.auth.index import userblueprint
from route.todo.index import todoblueprint
from route.admin.index import adminblueprint
import os


app = Flask("__name__")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#load .env
load_dotenv(find_dotenv())
#get secret key
SECRET_KEY = os.environ.get("SECRET")


app.register_blueprint(userblueprint, url_prefix='/api/user')
app.register_blueprint(todoblueprint, url_prefix='/api/todo')
app.register_blueprint(adminblueprint, url_prefix='/api/admin')
