from app import app
from flask_jwt import JWT
from werkzeug.security import safe_str_cmp

from app.models import User

# Move to DB
users = [
    User(1, 'wishcoin', 'media', 'admin'),
    User(2, 'sanjith', 'react', 'front-end'),
    User(3, 'johndoe', 'password', 'user'),
]

def update_tables(users):
    username_table = {u.username: u for u in users}
    userid_table = {u.id: u for u in users}
    return username_table, userid_table
def authenticate(username, password):
    # Fetch user information from DB instead
    username_table, _ = update_tables(users)
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']

    # Fetch user information from DB instead
    _, userid_table = update_tables(users)
    return userid_table.get(user_id, None)

jwt = JWT(app, authenticate, identity)
