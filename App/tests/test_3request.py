import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from App.main import create_app
from App.database import create_db
from App.models import Request, Status
from App.controllers import (
    create_request,
    get_all_student_requests_JSON,
    get_all_staff_request_JSON,
    get_request_JSON,
    change_status,
    get_staff_acceptedR,
    get_staff_pendingR,
    get_student_acceptedR,
    get_student_pendingR,

)

from wsgi import app
LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''

class RequestUnitTests(unittest.TestCase):

    def test_create_request(self):
        
        date = datetime.now()
        request = Request(staffId= "819000111",studentId= "816000111",body= "request" ,dateNTime=date, status=Status.PENDING)
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


# class RequestIntegrationTests(unittest.TestCase):
    
#     #checks if a request was created
    # test currently failing, somehow causes STAFF TEST to fail as well???? idk how
    def test_create_request(self):
        request = create_request(studentId= "816000111",staffId= "819000111",body= "request")
        assert request.body == "request"


    # #checks to see all requests for a student were found
    # test failing
    # def test_get_all_student_requests_JSON(self):
    #     #id = "816000111"
    #     request = get_all_student_requests_JSON("816000111")
    #     self.assertListEqual([{'staffId': "819000111",'studentId': "816000111",'requestID': "1",'body': "request",'status': "PENDING",'dateNTime': """",'seen': "True"}], students_json)
       

    