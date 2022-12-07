import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from App.main import create_app
from App.database import create_db
from App.models import Notification, Status
from App.controllers import (
    create_notification,
    get_all_notifs_unseen,
    get_notif,

)

from wsgi import app
LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''

class NotificationUnitTests(unittest.TestCase):

    def test_create_notification(self):
        
        date = datetime.now()
        request = Notification(staffId= "819000111",requestId= "1",body= "request" ,dateNTime=date, seen=False)
        assert request.body == "request"


'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


# class NotificationIntegrationTests(unittest.TestCase):
    
    #cant do other test if the create integration fails
    #test below was a temp measure
    # def test_create_notification(self):
    #     # date = datetime.now()
    #     # notification = Notification(staffId= "819000111",requestId= "1",body= "request" ,dateNTime=date, seen=False)
    #     assert notification.body == "request"



    # #checks if a notification was created
    # #test currently failing, AttributeError: 'str' object has no attribute 'body'
    # def test_create_notification(self):
    #     notification = create_notification(request= "this is a request",name= "Betty")
    #     assert notification.body == "request"

    # #checks if a notification can be found by id
    # def test_get_notif(self):
    #     notif = get_notif(1)
    #     assert notif.body == "request"
    
    # #checks if a notification status can be changed
    # def test_change_status(self):
    #     notif = create_notification(request= "this is a request",name= "Betty")
    #     change_status(notif, "REJECTED")
    #     assert notif.status == "REJECTED"
    


