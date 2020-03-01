from app import db
from datetime import datetime


class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    occupation = db.Column(db.String)
    income = db.Column(db.String)
    birthplace = db.Column(db.String)
    current_city = db.Column(db.String)
    religion = db.Column(db.String)


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    answers = db.Column(db.String)
    party_1_id = db.Column(db.Integer, db.ForeignKey('parties.id'))
    party_2_id = db.Column(db.Integer, db.ForeignKey('parties.id'))
    party_3_id = db.Column(db.Integer, db.ForeignKey('parties.id'))


class Parties(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String)
    answers = db.Column(db.String)


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

