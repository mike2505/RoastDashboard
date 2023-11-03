from flask import Flask
from flask_cors import CORS
from app.extensions import db, migrate

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.controllers import auth
    app.register_blueprint(auth.auth_blueprint)


    return app