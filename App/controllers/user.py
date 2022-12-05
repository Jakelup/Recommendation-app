from App.models import User, Student, Staff
from App.database import db
from sqlalchemy.exc import IntegrityError
from flask import Response, flash
from flask_login import LoginManager



# Create new User
# def create_user(username, password, name, faculty, department, userType):
#     if (userType=="student"):
#         newuser = Student(username=username, password=password, name=name, faculty=faculty, department=department, userType=userType)
#     else:
#         if (userType=="staff"):
#             newuser = Staff(username=username, password=password, name=name, faculty=faculty,department=department, userType=userType)
#     return newuser


# get User by id
def get_user(id):
    return User.query.get(id)

# get all User objects
def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return None
    users = [user.toJSON() for user in users]
    return users

def validate_Staff(username, password):
    staff = Staff.query.filter_by(username = username).all()
    for s in staff:
        if s and s.check_password(password):
            return s
    return None

def validate_Student(username, password):
    student = Student.query.filter_by(username = username).all()
    for s in student:
        if s and s.check_password(password):
            return s
    return None
        
    
