from app import db
from datetime import datetime

class AIAnalysisResults(db.Model):
    __tablename__ = 'ai_analysis_results'

    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey('landing_pages.id'), nullable=False)
    analysis_data = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)