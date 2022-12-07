import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from App.main import create_app
from App.database import create_db
from App.models import  Recommendation
from App.controllers import (
    get_all_recommendations_json,
    get_staff_by_recommendation,
    create_recommendation,
    submit_recommendation,
    get_recommendation,
)


from wsgi import app
LOGGER = logging.getLogger(__name__)


class RecommendationUnitTests(unittest.TestCase):

    def test_create_recommendation(self):
        date = datetime.now().date()
        recommendation= Recommendation(staffId= "819000111",studentId= "816000111",body= "recommendation" ,date=date)
        assert recommendation.body == "recommendation"

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


# class RecommendationIntegrationTests(unittest.TestCase):
    
    #test to see if create recommendation controller is working - currently failing
    # def test_create_recommendation(self):
    #     recom = create_recommendation(sentFromStaffID = "819000111", sentToStudentID = "816000111", body = "Recommendation Made")
    #     assert recom.body == "Recommendation Made"
    
    # def test_get_all_recommendations_json(self):
    #     date = datetime.now().date()
    #     # recommendation= Recommendation(staffId= "819000111",studentId= "816000111",body= "recommendation" ,date=date)
    #     recs_json = get_all_recommendations_json()
    #     self.assertListEqual([{'recId'== "1",'staffId'== "819000111", 'studentId'== "816000111" ,'body'== "Recommendation Made",'date'==date}], recs_json)
    
    
    # def test_get_recommendation(self):
    #     recom= get_recommendation("816000111", "1")
    #     assert recom.body == "Recommendation Made"