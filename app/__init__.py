from flask import Flask
from app.controllers.auth import auth_blueprint

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(example_blueprint)

# More app configuration can go here