from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CandidateScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    match_score = db.Column(db.Float)
