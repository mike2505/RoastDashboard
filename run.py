from app import create_app, db
from app.config import DevelopmentConfig
from app.extensions import db

app = create_app(DevelopmentConfig)

if __name__ == "__main__":
    app.run()