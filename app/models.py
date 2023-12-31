from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # hier dann die liste an toubles einfügen
    datapoints = db.relationship('Datapoint', backref='person', lazy='dynamic')
    weekly_change = db.Column(db.String, index=True, unique=True, default='None')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Datapoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    weight = db.Column(db.Float)

    def __repr__(self):
        return '<Datapoint, timestamp: {}, weight: {}>'.format(self.timestamp, self.weight)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))