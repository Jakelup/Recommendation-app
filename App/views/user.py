from flask import Flask
from flask import Blueprint, flash, redirect, render_template, jsonify, request, send_from_directory, url_for
from flask_jwt import jwt_required, current_identity
from flask_login import LoginManager, current_user, login_required
from App.database import db
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_url_path='/static')

login_manager = LoginManager()
login_manager.login_view = 'login'


from App.controllers import (
    # create_user,
    get_all_users,
    get_all_users_json,
    get_all_students_json,
    get_user,
    staff_signup,
    student_signup,
    validate_Staff,
    validate_Student,
    login_user
)

from App.models import (
    StudentLogIn,
    StaffLogIn,
    StudentRegister,
    StaffRegister
)


user_views = Blueprint('user_views', __name__, template_folder='../templates')



    
## LOG IN:

##STUDENT LOGIN PAGES
@user_views.route('/login/Student')
def getLoginPage():
    if current_user.is_authenticated:
        flash('Already Logged In')
        return redirect(url_for('student_views.studentMain'))
    form = StudentLogIn()
    return render_template('login.html', form=form, usertype="Student")



@user_views.route('/login/Student', methods = {'POST'})
def LoginAction():
    form = StudentLogIn()
    data = request.form
    if form.validate_on_submit():
        user = validate_Student(data['username'], data['password'])
        if user:
            login_user(user, True)
            flash('Successful Login')
            return redirect(url_for('student_views.studentMain'))

    flash('Invalid. Check username and/or password')
    return render_template('login.html', form=form, usertype="Student")
    # return redirect(url_for('user_views.LoginAction'))



##STAFF LOGIN PAGES
@user_views.route('/login/Staff')
def getStaffLoginPage():
    if current_user.is_authenticated:
        flash('Already Logged In')
        return redirect(url_for('staff_views.staffMain'))
    form = StaffLogIn()
    return render_template('login.html', form=form, usertype="Staff")

@user_views.route('/login/Staff', methods = {'POST'})
def loginStaff():
    form = StaffLogIn()
    data = request.form
    if form.validate_on_submit():
        user = validate_Staff(data['username'], data['password'])
        if user:
            login_user(user, True)
            flash('Successful Login')
            return redirect(url_for('staff_views.staffMain'))

    flash('Invalid. Check username and/or password')
    return redirect(url_for('user_views.loginStaff'))




## LOGOUT
@user_views.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return render_template('index.html')





# SIGNUP - CREATE ACCOUNT


##STUDENT SIGN UP PAGES
@user_views.route('/signup/Student', methods = ['GET'])
def getStudentSignUpPage():
    if current_user.is_authenticated:
        flash('You cannot create an account while logged in.')
        return redirect(url_for('student_views.studentMain'))
    form = StudentRegister()
    return render_template('signUp.html', form=form, usertype="Student")

@user_views.route('/signup/Student', methods = ['GET', 'POST'])
def studentSignUpAction():
    form = StudentRegister()
    data = request.form 
    student = student_signup(data['sID'], data['username'], data['password'], data['name'], data['faculty'], data['department'])
    if student == None:
        flash('Error in creating account')
        # return redirect(url_for('user_views.getStudentSignUpPage'))
        return render_template('signUp.html', form=form, usertype="Student")
    else:
        flash('Account Created!')
    # return redirect(url_for('user_views.LoginAction'))
    return render_template('login.html', form=form, usertype="Student")





##STAFF SIGN UP PAGES
@user_views.route('/signup/Staff')
def getStaffSignUpPage():
    if current_user.is_authenticated:
        flash('You cannot create an account while logged in.')
        return redirect(url_for('staff_views.staffMain'))
    form = StaffRegister()
    return render_template('signUp.html', form=form, usertype="Staff")

@user_views.route('/signup/Staff', methods = {'POST'})
def staffSignUpAction():
    form = StaffRegister()
    data = request.form 
    staff = staff_signup(data['sID'], data['username'], data['password'], data['name'], data['faculty'], data['department'])
    if staff == None:
        flash('Error in creating account')
        # return redirect(url_for('getStaffSignUpPage'))
        return render_template('signUp.html', form=form, usertype="Staff")
    else:
        flash('Account Created!')
        # return redirect(url_for('user_views.loginStaff'))
        return render_template('login.html', form=form, usertype="Staff")






# Routes for testing purposes
# check identity of current user
@user_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    return jsonify({'message': f"id : {current_identity.id}, email: {current_identity.email}, userType: {current_identity.userType}"})

# View all Users
@user_views.route('/view/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

# JSON View all Users
@user_views.route('/users')
def client_app():
    users = get_all_students_json()
    return jsonify(users)

# STATIC View all Users
@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')

