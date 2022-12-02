from flask import Flask
from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity
from flask_login import LoginManager, current_user, login_required
from App.database import db
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_url_path='/static')

login_manager = LoginManager()
login_manager.login_view = 'login'


from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    get_user,
    user_signup
)

from App.models import (
    StudentLogIn,
    StaffLogIn,
    StudentRegister,
    StaffRegister
)


user_views = Blueprint('user_views', __name__, template_folder='../templates')


# SIGNUP - CREATE ACCOUNT


##STUDENT SIGN UP PAGES
@user_views.route('/signup/Student', methods=['GET', 'POST'])
def getStudentSignUpPage():
    if current_user.is_authenticated:
        flash('You cannot create an account while logged in.')
        return render_template('studentMain.html')
    form = StudentRegister()
    return render_template('signUp.html', form=form, usertype="Student")

@app.route('/signup/Student', methods=['POST'])
def studentSignUpAction():
    form = StudentRegister()()
    data = request.form 
    msg = user_signup(data['username'], data['password'], data['name'], data['faculty'], data['department'], userType="student")
    if msg == "Error":
        flash('Error in creating account')
        return redirect(url_for('getStudentSignUpPage'))
    else:
        flash('Account Created!')
        return render_template('login.html', form=form, usertype="Student")




##STAFF SIGN UP PAGES
@user_views.route('/signup/Staff', methods=['GET', 'POST'])
def getStaffSignUpPage():
    if current_user.is_authenticated:
        flash('You cannot create an account while logged in.')
        return render_template('studentMain.html')
    form = StudentRegister()
    return render_template('signUp.html', form=form, usertype="Staff")

@app.route('/signup/Staff', methods=['POST'])
def staffSignUpAction():
    form = StudentRegister()()
    data = request.form 
    msg = user_signup(data['username'], data['password'], data['name'], data['faculty'], data['department'], userType="staff")
    if msg == "Error":
        flash('Error in creating account')
        return redirect(url_for('getStaffSignUpPage'))
    else:
        flash('Account Created!')
        return render_template('login.html', form=form, usertype="Staff")




    
## LOG IN:

##STUDENT LOGIN PAGES
@user_views.route('/login/Student')
def getLoginPage():
    if current_user.is_authenticated:
        flash('Already Logged In')
        return render_template('studentMain.html')
    form = StudentLogIn()
    return render_template('login.html', form=form, usertype="Student")



@user_views.route('/login/Student', methods=['GET', 'POST'])
def login():
    form = StudentLogIn()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, True)
                flash('Successful Login')
                return render_template('studentMain.html', form=form, usertype="Student")
    flash('Invalid. Check username and/or password')
    return render_template('login.html', form=form, usertype="Student")



##STAFF LOGIN PAGES
@user_views.route('/login/Staff')
def getStaffLoginPage():
    if current_user.is_authenticated:
        flash('Already Logged In')
        return render_template('staffMain.html')
    form = StaffLogIn()
    return render_template('login.html', form=form, usertype="Staff")



@user_views.route('/login/Staff', methods=['GET', 'POST'])
def loginStaff():
    form = StaffLogIn()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, True)
                flash('Successful Login')
                return render_template('staffMain.html', form=form, usertype="Staff")
    flash('Invalid. Check username and/or password')
    return render_template('login.html', form=form, usertype="Staff")





@user_views.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return render_template('index.html')




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
    users = get_all_users_json()
    return jsonify(users)

# STATIC View all Users
@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')

