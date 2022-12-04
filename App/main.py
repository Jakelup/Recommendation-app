import os
from flask import Flask, render_template
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import timedelta
from flask_login import LoginManager, current_user

from App.database import create_db

from App.controllers import (
    setup_jwt,
)

from App.models import (
    User,
    Student,
    Staff
)

from App.views import (
    user_views,
    index_views,
    student_views,
    staff_views,
    notification_views,
    recommendation_views,
    request_views
)

# New views must be imported and added to this list
views = [
    user_views,
    index_views,
    student_views,
    staff_views,
    notification_views,
    recommendation_views,
    request_views
]


app = Flask(__name__, static_url_path='/static')

login_manager = LoginManager(app)
# login_manager.init_app(app) -- moved this to create_app function below

@login_manager.user_loader
def load_user(user_id):
    student = Student.query.get(user_id)
    if student:
        return student
    else:
        return Staff.query.get(user_id)

    # try: 
    #     return Student.query.get(user_id)
    #     try:
    #         return Staff.query.get(user_id)
    #     except: 
    #         return None
    # except: 
    #     return None

    # if current_user == None:
    #     return render_template('index.html')
    # # else:
    #     return current_user

    # if current_user.userType == 'Staff':
    #     return Staff.query.get(int(user_id))
    # elif current_user.userType == 'Student':
    #     return Student.query.get(int(user_id))
    # elif current_user == None:
    #     return None
        # return render_template('index.html')
#should return obj even if none


def add_views(app, views):
    for view in views:
        app.register_blueprint(view)


def loadConfig(app, config):
    app.config['ENV'] = os.environ.get('ENV', 'DEVELOPMENT')
    delta = 7
    if app.config['ENV'] == "DEVELOPMENT":
        app.config.from_object('App.config')
        delta = app.config['JWT_EXPIRATION_DELTA']
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['DEBUG'] = os.environ.get('ENV').upper() != 'PRODUCTION'
        app.config['ENV'] = os.environ.get('ENV')
        delta = os.environ.get('JWT_EXPIRATION_DELTA', 7)
        
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=int(delta))
        
    for key, value in config.items():
        app.config[key] = config[key]


def create_app(config={}):
    app = Flask(__name__, static_url_path='/static')
    CORS(app)
    loadConfig(app, config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    login_manager.init_app(app)
    add_views(app, views)
    create_db(app)
    setup_jwt(app)
    app.app_context().push()
    return app


