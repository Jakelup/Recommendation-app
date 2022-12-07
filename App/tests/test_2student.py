import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import Student
from App.controllers import (
    create_student,
    get_student,
    get_all_students_json,
    create_request,
    get_all_student_requests_JSON,
    get_all_recommendations_json,
    get_student_reclist_json
)

from wsgi import app
LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''

class StudentUnitTests(unittest.TestCase):

    def test_create_student(self):
        student = Student(username= "sponge",password= "pass123",name = "spongebob",id= "816000111",faculty= "FST",department= "DCIT")
        assert student.name == "spongebob"
    


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


# class StudentIntegrationTests(unittest.TestCase):
    
#     #checks if a student user was created
    def test_create_student(self):
        student = create_student(id="816000000", username="Boop", password="pass123", name="Betty", faculty= "FST", department="DCIT")
        assert student.name == "Betty"


    # #checks to see if a student was be found by ID
    # def test_search_all_students(self):
    #     id = "816000000"
    #     student = get_student("816000000")
    #     assert student.name == "Betty"


    #checks to see if all students were found
    #def test_get_all_students_json(self):
    #     #add another user so student wont be none
    #     student = create_student(id="816000000", username="boop", password="pass123", name="Betty", faculty= "FST", department="DCIT")
    #     s = create_student(id="816000111", username="spongebob", password="pass123", name="Spongebob", faculty= "FST", department="DCIT")
    #     students_json = get_all_students_json()
    #     self.assertListEqual([{"id"=="816000000", "username"=="boop", "password"=="pass123", "name"=="Betty", "faculty"=="FST", "department"=="DCIT"}], students_json)
        #shows none even though 2 students are added and create student passed test

    #checks to see if all recommendations were retrieved
    # def test_get_all_recommendations_json(self):
    #     recs_json = get_all_recommendations_json()
    #     self.assertListEqual([{"recId"=="", "staffId"=="", "studentId"=="", "body"=="", "date"==""}],recs_json)

    #checks to see if a student's recommendations list was retrieved
    # def test_get_student_reclist_json(self):
    #     recs_json = get_student_reclist_json("816000000")
    #     self.assertListEqual(recs_json)

    # def test_create_request(self):
    #     request = create_request(staffId="819000111", studentId="816000111", body="Request Made")
    #     assert request.body == "Request Made"
    #     #TypeError: __init__() missing 1 required positional argument: 'requestId'