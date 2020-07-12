from flask import request
from flask_jwt import jwt_required, current_identity
from app import app
from app.models import User

from app.auth import users

# DEBUG route
@app.route('/whoami')
@jwt_required()
def protected():
    # use the user ID to make more DB calls
    return '%s' % current_identity

# Admin operations

@app.route('/user', methods=['POST'])
@jwt_required()
def user():
    """Add a new user"""
    if current_identity.role != 'admin':
        return "Admin access required for this operation", 401
    # Write to DB instead
    users.append(User(len(users) + 1, request.json['username'], request.json['password'], request.json['role']))
    return "User created successfuly", 200

# User operations

@app.route('/password', methods=['PATCH'])
@jwt_required()
def password():
    """Change a particular user's password"""
    current_identity.password = request.json['password']
    return "Password updated successfully", 200
