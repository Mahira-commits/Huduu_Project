from urllib.parse import uses_relative
from . import db
from flask_login import UserMixin
import datetime

class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80),nullable=False)
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    ##check how to convert string type to BOOL type
    userType=db.Column(db.Boolean, nullable=False)
   ## Appointments = db.relationship('Appointments', backref=db.backref('User', lazy=True))
'''
    def __repr__(self):
        return f'<User {self.username}>'
'''
class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    #happy, neutral, sad
    feeling = db.Column(db.String(10), nullable=False)
    #1,2,3+ for 1,2,3+ meals
    num_meals = db.Column(db.String(2), nullable=False)
    # 0-3,4-6,7-9,10+
    num_hrs = db.Column(db.String(5), nullable=False)
'''
class Appointments(db.Model):
    name=db.Column(db.String(150), nullable=False)
    studentId=db.Column(db.Integer,db.ForeignKey('User.id'),primary_key=True, nullable=False)
    counselorId=db.Column(db.Integer,db.ForeignKey('User.id'), nullable=False)
    date=db.Column(db.String(10),primary_key=True, nullable=False)
    time=db.Column(db.String(10),primary_key=True, nullable=False)
    message = db.Column(db.String(1000))

class StudentTips(db.Model):
    studentId=db.Column(db.Integer,db.ForeignKey('User.id'),primary_key=True,  nullable=False)
    counselorId=db.Column(db.Integer,db.ForeignKey('User.id'), primary_key=True, nullable=False)
    message = db.Column(db.String(1000), nullable=False)

class BroadcastTips(db.Model):
    studentId=db.Column(db.Integer,db.ForeignKey('User.id'),primary_key=True, nullable=False)
    message = db.Column(db.String(1000), nullable=False, primary_key=True)
'''