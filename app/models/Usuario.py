
from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(255))
    senha = db.Column(db.String(255))
