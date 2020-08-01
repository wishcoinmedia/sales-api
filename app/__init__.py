from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)

'''Enable CORS for all requests'''
CORS(app)

'''Load configuration depending on environment'''
if app.config["ENV"] == "production":
    app.config.from_object('wcm-sales.ProdConfig')
elif app.config["ENV"] == "development":
    app.config.from_object('wcm-sales.DevConfig')
else:
    app.config.from_object('wcm-sales.Config')

'''MongoDB configuration'''
mongo = PyMongo(app)

from app import routes, models, auth
