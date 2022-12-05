import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import User
from App.controllers import (
    #create_user,
    authenticate,
    get_user,
    get_all_users,
    get_all_users_json,
    create_student,
    create_staff,
    validate_Staff,
    validate_Student
)


from wsgi import app
LOGGER = logging.getLogger(__name__)
