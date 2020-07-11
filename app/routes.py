from flask import request
from flask_jwt import jwt_required, current_identity
from app import app

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'You are being logged in ...'
    else:
        return 'This is the login form'

@app.route('/protected')
@jwt_required()
def protected():
    # use the user ID to make more DB calls
    return '%s' % current_identity
