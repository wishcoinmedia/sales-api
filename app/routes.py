from flask import request
from flask_jwt import jwt_required, current_identity
from app import app, mongo
from app.models import User
from pymongo import errors
import json

# DEBUG route
@app.route('/whoami')
@jwt_required()
def protected():
    try:
        user = mongo.db.users.find_one_or_404({"username": "wishcoin"})
    except errors.PyMongoError as e:
        app.logger.error("PyMongoError: %s" % e)
    return '{}\n{}'.format(current_identity, user)

# Admin operations

@app.route('/user', methods=['GET', 'POST', 'DELETE'])
@jwt_required()
def user():
    """Add a new user"""
    if current_identity.role != 'admin':
        return "Admin access required for this operation", 401

    try:
        if request.method == 'GET':
            return json.dumps(dict(User.from_dict(mongo.db.users.find_one_or_404({'id': request.json['id']}))))
        elif request.method == 'POST':
            count = mongo.db.users.count({})
            user = User(count+1, request.json['username'], request.json['password'], request.json['role'])
            mongo.db.users.insert_one(dict(user))
            return "User created successfuly", 200
        elif request.method == 'DELETE':
            mongo.db.users.find_one_and_delete({"id": request.json['id']})
            return "User deleted successfuly", 200
    except errors.PyMongoError as e:
        app.logger.error("PyMongoError: %s" % e)
        return "Server under maintenance. Please try again later", 503
    except KeyError:
        return 400

# User operations

@app.route('/password', methods=['PATCH'])
@jwt_required()
def password():
    """Change a particular user's password"""
    try:
        mongo.db.users.update_one({"id": current_identity.id}, {"$set": {"password": request.json['password']}})
        return "Password updated successfully", 200
    except error.PyMongoError as e:
        app.logger.error("PyMongoError: %s" % e)
        return "Server under maintenance. Please try again later", 503
    except KeyError:
        return 400
