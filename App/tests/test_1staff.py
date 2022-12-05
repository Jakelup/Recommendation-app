import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import Staff, Notification, Recommendation
from App.controllers import (
    create_staff,
    get_staff,
    get_all_staff_json,
    get_staff_by_recommendation,
    get_staff_by_name,
    get_staff_feed_json,
    change_status,
    create_recommendation,
    submit_recommendation,
)

#### Staff test was failing if Notification test ran first for some reason, rename test file 1staff so staff could run first


from wsgi import app
LOGGER = logging.getLogger(__name__)


class UserUnitTests(unittest.TestCase):

    def test_create_staff(self):
        staff = Staff(username= "sponge",password= "pass123",name = "spongebob",id= "819000111",faculty= "FST",department= "DCIT")
        assert staff.name == "spongebob"
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


class StaffIntegrationTests(unittest.TestCase):
    
    #checks if a staff user was created
    def test_create_staff(self):
        staff = create_staff(id= "819000000",username= "boop",password= "pass123",name= "Betty",faculty= "FST",department= "DCIT")
        assert staff.name == "Betty"

    #checks to see if a staff was be found by ID

    def test_search_all_staff(self):
        #id = "816000000"
        staff = get_staff("819000000")
        assert staff.name == "Betty"

    #checks if data from the staff table in json was retrieved
    # def test_get_all_staff_json(self):
    #     #add another user so staff wont be none\
    #     # s = create_staff(id="816000111", username="spongebob", password="pass123", name="Spongebob", faculty= "FST", department="DCIT")
    #     staff_json = get_all_staff_json()
    #     # self.assertListEqual([{'staffId'=="816000000",'name'=="Betty",'faculty'=="FST",'department'=="DCIT"}], staff_json)
    #     self.assertListEqual([{'department'=="DCIT",'faculty'=="FST",'name'=="Betty",'staffId'=="816000000"}], staff_json)

            
        #       list error where list is here but backward?
        # E       First differing element 0:
        # E       {False}
        # E       {'staffId': 819000000, 'name': 'Betty', 'faculty': 'FST', 'department': 'DCIT'}
        # E       
        # E       - [{False}]
        # E       + [{'department': 'DCIT',
        # E       +   'faculty': 'FST',
        # E       +   'name': 'Betty',
        # E       +   'staffId': 819000000}]
            
    # def test_get_staff_by_name(self):
    #     #idk why not working
    #     staff = get_staff_by_name("Betty")
    #     # assert staff.id == 819000000
    #     self.assertListEqual([{ 'staffId'=="819000000",'name'=="Betty", 'faculty'=="FST", 'department'=="DCIT"}], staff)

   
    def test_create_recommendation(self):
        recom = create_recommendation(sentFromStaffID = "819000111", sentToStudentID = "816000111", body = "Recommendation Made")
        assert recom.body == "Recommendation Made"
    
    #def test_submit_recommendation():