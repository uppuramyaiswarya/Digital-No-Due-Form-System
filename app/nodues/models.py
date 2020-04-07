
from app.application import db


class Library(db.Model):
    __tablename__ = 'library'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='library', uselist=False)
    one = db.Column(db.Integer)
    two = db.Column(db.Integer)
    three = db.Column(db.Integer)
    four = db.Column(db.Integer)


class Pdp(db.Model):
    __tablename__ = 'pdp'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='pdp', uselist=False)
    one = db.Column(db.Integer)
    two = db.Column(db.Integer)
    three = db.Column(db.Integer)
    four = db.Column(db.Integer)


class College(db.Model):
    __tablename__ = 'college'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='college', uselist=False)
    one = db.Column(db.Integer)
    two = db.Column(db.Integer)
    three = db.Column(db.Integer)
    four = db.Column(db.Integer)