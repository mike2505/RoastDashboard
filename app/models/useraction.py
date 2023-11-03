from app import db
from datetime import datetime

class UserAction(db.Model):
    __tablename__ = 'user_actions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    action_type = db.Column(db.String(50))
    action_details = db.Column(db.Text)
    action_date = db.Column(db.DateTime, default=datetime.utcnow)