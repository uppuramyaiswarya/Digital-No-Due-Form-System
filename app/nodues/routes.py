from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user


from . import nodues
from app.users.models import User
from .models import Library, Pdp, College

@nodues.route('/nodues')
def index():
    return "nodues"


@nodues.route('/get-status')
@login_required
def get_status():
    roll_no = request.args.get('roll_no')
    if current_user.is_admin == True or current_user.roll_no == roll_no:
        user = User.query.filter_by(roll_no=roll_no).first()
        print("user is",roll_no)
        data, total_dues = generate_total_due_data(roll_no)
        return render_template('profile.html', user=user, data=data, total_dues=total_dues)


def generate_total_due_data(roll_no):
    user = User.query.filter_by(roll_no=roll_no).first()
    pdp = user.pdp[0]
    college = user.college[0]
    library = user.library[0]
    pdp_due = {
        'one': pdp.one,
        'two': pdp.two,
        'three': pdp.three,
        'four': pdp.four
    }
    college_due = {
        'one': college.one,
        'two': college.two,
        'three': college.three,
        'four': college.four
    }
    library_due = {
        'one': library.one,
        'two': library.two,
        'three': library.three,
        'four': library.four
    }
    total_pdp_due, total_library_due, total_college_due = 0, 0, 0
    for key, value in pdp_due.items():
        total_pdp_due += value
    for key, value in library_due.items():
        total_library_due += value
    for key, value in college_due.items():
        total_college_due += value
    total_dues = [total_pdp_due, total_library_due, total_college_due]
    data = [pdp_due, library_due, college_due]
    return data, total_dues