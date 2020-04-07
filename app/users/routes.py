from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse

from . import users
from .models import User
from app.nodues.routes import generate_total_due_data
from app.application import db


@users.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('users.dashboard'))
        else:
            return redirect(url_for('users.profile'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                if user.is_admin:
                    next_page = url_for('users.dashboard')
                else:
                    next_page = url_for('users.profile')
            return redirect(next_page)
        else:
            flash('Invalid credentials')
            return redirect(url_for('users.login'))
    return render_template('login.html')


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@users.route('/changepassword',methods=['GET','POST'])
@login_required
def changepassword():
    user=current_user
    if request.method == 'POST':
        password = request.form.get('password')
        newpassword = request.form.get('new-password')
        confirmationpassword = request.form.get('confirmation-password')
        if user and user.check_password(password):
            if newpassword==confirmationpassword:
                user.set_password(newpassword)
                db.session.add(user)
                db.session.commit()
                flash('change password succesful')
            else:
                flash('new and confirmation passwords are missmatched')
        else:
            flash('present password not correct')
    return render_template('changepassword.html')



@users.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')


@users.route('/profile')
@login_required
def profile():
    due_data, total_dues = [], []
    if not current_user.is_admin:
        due_data, total_dues = generate_total_due_data(current_user.roll_no)
=======
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse

from . import users
from .models import User
from app.nodues.routes import generate_total_due_data
from app.application import db


@users.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('users.dashboard'))
        else:
            return redirect(url_for('users.profile'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                if user.is_admin:
                    next_page = url_for('users.dashboard')
                else:
                    next_page = url_for('users.profile')
            return redirect(next_page)
        else:
            flash('Invalid credentials')
            return redirect(url_for('users.login'))
    return render_template('login.html')


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@users.route('/changepassword',methods=['GET','POST'])
@login_required
def changepassword():
    user=current_user
    if request.method == 'POST':
        password = request.form.get('password')
        newpassword = request.form.get('new-password')
        confirmationpassword = request.form.get('confirmation-password')
        if user and user.check_password(password):
            if newpassword==confirmationpassword:
                user.set_password(newpassword)
                db.session.add(user)
                db.session.commit()
                flash('change password succesful')
            else:
                flash('new and confirmation passwords are missmatched')
        else:
            flash('present password not correct')
    return render_template('changepassword.html')



@users.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')


@users.route('/profile')
@login_required
def profile():
    due_data, total_dues = [], []
    if not current_user.is_admin:
        due_data, total_dues = generate_total_due_data(current_user.roll_no)
    return render_template('profile.html', user=current_user, data=due_data, total_dues=total_dues)
