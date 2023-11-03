from flask import Blueprint
from app.views.auth import register, login

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register')
def register():
    return register()

@auth_blueprint.route('/login')
def register():
    return login()