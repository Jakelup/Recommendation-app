import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import User
from App.controllers import (
    #create_user,
    authenticate,
)


from wsgi import app
LOGGER = logging.getLogger(__name__)

class UserUnitTests(unittest.TestCase):
    def test_create_user(self):
            user = User(id= "816000001",password= "pass123",username= "sponge",name = "spongebob",faculty= "FST",department= "DCIT")
            assert user.name == "spongebob"
            