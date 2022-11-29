from App.models import User, Student, Staff
from App.database import db
from sqlalchemy.exc import IntegrityError
from flask import Response

# Create new User
def create_user(email, password, userType, firstName, lastName):
    if (userType=="student"):
        newuser = Student(email=email, password=password, userType=userType, firstName=firstName, lastName=lastName)
    else:
        if (userType=="staff"):
            newuser = Staff(email=email, password=password, userType=userType, firstName=firstName, lastName=lastName)
    return newuser

# SIGNUP
def user_signup(firstName, lastName, email, password, userType):
    newuser = create_user(email=email,
        password=password,
        userType=userType,
        firstName=firstName,
        lastName=lastName)
    try:
        db.session.add(newuser)
        db.session.commit()
    except IntegrityError: # attempted to insert a duplicate user
        db.session.rollback()
        return Response({'user already exists with this email'}, status=400) #error message
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

