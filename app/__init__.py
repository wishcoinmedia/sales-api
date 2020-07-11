from flask import Flask

from config import Config

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
db = '' #place db object here

from app import routes, models, auth
