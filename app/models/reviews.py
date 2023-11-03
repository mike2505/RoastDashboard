from app import db
from datetime import datetime

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('landing_pages.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    review_content = db.Column(db.Text)
    humor_score = db.Column(db.Integer)
    insights_score = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)