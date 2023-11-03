from app import db
from datetime import datetime

class LandingPage(db.Model):
    __tablename__ = 'landing_pages'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    url = db.Column(db.String(2048))
    title = db.Column(db.String(200))
    submitted_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_reviewed_date = db.Column(db.DateTime)
    status = db.Column(db.String(50))