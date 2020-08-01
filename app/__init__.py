from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)

'''Enable CORS for all requests'''
CORS(app)
app.logger.info("Enabled CORS")

'''Load configuration depending on environment'''
if app.config["ENV"] == "production":
    app.config.from_object('wcm-sales.ProdConfig')
    app.logger.info('Configuration for production environment loaded.')
elif app.config["ENV"] == "development":
    app.config.from_object('wcm-sales.DevConfig')
    app.logger.info('Configuration for development environment loaded.')
else:
    app.config.from_object('wcm-sales.Config')
    app.logger.info('Configuration for basic environment loaded.')

'''MongoDB configuration'''
mongo = PyMongo(app)
app.logger.info('MongoDB configuration complete.')

from app import routes, models, auth
