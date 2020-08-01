from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('wcm-sales.DevConfig')
mongo = PyMongo(app)

from app import routes, models, auth
