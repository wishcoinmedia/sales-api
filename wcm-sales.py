"""Flask Config"""

from os import environ, path
from dotenv import load_dotenv

# Base directory of the application
base_dir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(base_dir, '.env'))


class Config(object):
    '''Base configuration.'''
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'


class ProdConfig(Config):
    '''Production configuration.'''
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')

    # mongodb-uri
    MONGO_URI = DATABASE_URI

class DevConfig(Config):
    '''Development configuration.'''
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')

    # mongodb-uri
    MONGO_URI = DATABASE_URI
