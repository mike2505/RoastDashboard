from app import db
from datetime import datetime

class Billing(db.Model):
    __tablename__ = 'billing'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    plan_type = db.Column(db.String(50))
    billing_date = db.Column(db.DateTime)
    amount = db.Column(db.Float)
    payment_status = db.Column(db.String(50))