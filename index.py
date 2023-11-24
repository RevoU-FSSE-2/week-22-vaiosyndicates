from flask import Flask
from dotenv import load_dotenv, find_dotenv
from flask_cors import CORS
from route.auth.index import userblueprint
from route.post.index import postblueprint
from route.follow.index import followblueprint
import os


app = Flask("__name__")
CORS(app)

#load .env
load_dotenv(find_dotenv())
#get secret key
SECRET_KEY = os.environ.get("SECRET")


app.register_blueprint(userblueprint, url_prefix='/user')
app.register_blueprint(postblueprint, url_prefix='/post')
app.register_blueprint(followblueprint, url_prefix='/follow')