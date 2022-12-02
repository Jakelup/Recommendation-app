from App.models import User, Student, Staff
from App.database import db
from sqlalchemy.exc import IntegrityError
from flask import Response, flash

# Create new User
# def create_user(username, password, name, faculty, department, userType):
#     if (userType=="student"):
#         newuser = Student(username=username, password=password, name=name, faculty=faculty, department=department, userType=userType)
#     else:
#         if (userType=="staff"):
#             newuser = Staff(username=username, password=password, name=name, faculty=faculty,department=department, userType=userType)
#     return newuser


# STUDENT SIGNUP
def student_signup(id, username, password, name, faculty, department):
    newStudent = Student(id=id, username=username, password=password, name=name, faculty=faculty, department=department)
    try:
        db.session.add(newStudent)
        db.session.commit()
        return newStudent
    except IntegrityError: # attempted to insert a duplicate user or other errors
        db.session.rollback()
        return None
    #     return Response({'user already exists with this username'}, status=400) #error message
    # return Response({'user created successfully'}, status=201) # success


# STAFF SIGNUP
def staff_signup(id, username, password, name, faculty, department):
    newStaff = Staff(id=id, username=username, password=password, name=name, faculty=faculty, department=department)
    db.session.add(newStaff)
    db.session.commit()
    return newStaff
    # newUser = User(username=username, password=password, name=name, faculty=faculty, department=department, userType="staff")
    # try:
    #     db.session.add(newStaff)
    #     db.session.commit()
    #     # db.session.add(newUser)
    #     # db.session.commit()
    #     return newStaff
    # except IntegrityError: # attempted to insert a duplicate user
    #     db.session.rollback()
    #     return None
    

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
        
    
