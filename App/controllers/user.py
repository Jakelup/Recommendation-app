from App.models import User, Student, Staff
from App.database import db
from sqlalchemy.exc import IntegrityError
from flask import Response

# Create new User
def create_user(username, password, name, faculty, department, userType):
    if (userType=="student"):
        newuser = Student(username=username,
        password=password,
        name=name,
        faculty=faculty,
        department=department,
        userType=userType)
    else:
        if (userType=="staff"):
            newuser = Staff(username=username,
        password=password,
        name=name,
        faculty=faculty,
        department=department,
        userType=userType)
    return newuser

# SIGNUP
def user_signup(username, password, name, faculty, department, userType):
    newuser = create_user(username=username,
        password=password,
        name=name,
        faculty=faculty,
        department=department,
        userType=userType)
    try:
        db.session.add(newuser)
        db.session.commit()
    except IntegrityError: # attempted to insert a duplicate user
        db.session.rollback()
        return Response({'user already exists with this username'}, status=400) #error message
    return Response({'user created successfully'}, status=201) # success

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

def validate_User(username, password):
    if User != None: #table empty
        user = User.query.filter_by(username = username).all()
        for u in user:
            if u and u.check_password(password):
                return u
        return None
    return None
