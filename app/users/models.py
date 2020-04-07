from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.application import db, login_manager


class Branch(db.Model):
    __tablename__ = 'branches'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    code = db.Column(db.String(10))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(40))

    def __str__(self):
        return self.code


class YearCode(db.Model):
    __tablename__ = 'yearcodes'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    section = db.Column(db.String(1))

    def __str__(self):
        return f'{self.year} - {self.semester} - {self.section}'


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    roll_no = db.Column(db.String(12))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    gender = db.Column(db.String(1))
    city = db.Column(db.String(50))
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.id'))
    branch = db.relationship('Branch', backref='students')
    yearcode_id = db.Column(db.Integer, db.ForeignKey('yearcodes.id'))
    yearcode = db.relationship('YearCode', backref='students')
    email = db.Column(db.String(40))
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    authenticated = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    '''
    def change_password(self, 

    '''

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False


@login_manager.user_loader
def load_user(id):
    print("Id is", id)
    return User.query.get(id)