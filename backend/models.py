from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), default='')
    layout = db.Column(db.String(20), default='card') # banner|card|cover
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    author = db.Column(db.String(100), default='MSD Admin')


class Alumni(db.Model):
    __tablename__ = 'alumni'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    major = db.Column(db.String(100), default='')
    role = db.Column(db.String(100), default='')
    company = db.Column(db.String(120), default='')
    quote = db.Column(db.String(255), default='')
    email = db.Column(db.String(120), default='')
    batch = db.Column(db.String(20), default='')