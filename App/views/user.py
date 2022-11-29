from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity
from flask_login import LoginManager, current_user
from App.database import db
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import Bcrypt

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    get_user,
    user_signup,
)

login_manager = LoginManager()
login_manager.initapp(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user.id):
    return User.query.get(int(user_id))

user_views = Blueprint('user_views', __name__, template_folder='../templates')


# SIGNUP - CREATE ACCOUNT
#@user_views.route('/signup', methods=['POST'])
#def createAccount():
#    data = request.get_json()
#    return user_signup(data['firstName'], data['lastName'], data['email'], data['password'], data['userType'])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        #redirect to approriate page
        return 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                #redirect to homepage
                return
    #redirect to homepage
    return

@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return render_template('login.html')

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
