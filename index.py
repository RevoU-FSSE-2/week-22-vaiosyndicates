from flask import Flask
from dotenv import load_dotenv, find_dotenv
from flask_cors import CORS
from route.auth.index import userblueprint
from route.todo.index import todoblueprint
import os


app = Flask("__name__")
CORS(app)

#load .env
load_dotenv(find_dotenv())
#get secret key
SECRET_KEY = os.environ.get("SECRET")


app.register_blueprint(userblueprint, url_prefix='/api/user')
app.register_blueprint(todoblueprint, url_prefix='/api/todo')