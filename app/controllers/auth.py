from flask import Blueprint
from app.views.auth import register_view, login_view

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register')
def register():
    return register_view()

@auth_blueprint.route('/login')
def login():
    return login_view()