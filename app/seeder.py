from app.users.models import Branch, YearCode
from app.application import db


def seed():
    """
    Use this method to populate the static data for branches and yearcodes
    :return: None
    """
    seed_branches()
    seed_yearcodes()
    db.session.commit()

def seed_branches():
    print("Seeding branches...")
    branches = [
        {'name': 'Electronics and Communication Engineering', 'code': 'ECE'},
        {'name': 'Electronics and Electronics Engineering', 'code': 'EEE'},
        {'name': 'Computer Science and Engineering', 'code': 'CSE'},
        {'name': 'Civil Engineering', 'code': 'CIVIL'},
        {'name': 'Mechanical Engineering', 'code': 'MECH'}
    ]
    db.session.add_all([ Branch(**data) for data in branches ])
    print("Seeding branches complete..")


def seed_yearcodes():
    print("Seeding yearcodes..")
    years = [1,2,3,4]
    semesters = [1,2]
    sections = ['A', 'B', 'C']
    for year in years:
        for semester in semesters:
            for section in sections:
                db.session.add(YearCode(year=year, semester=semester, section=section))
    print("Seeding yearcodes complete..")