import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import *
from App.controllers import (
    create_user,
    authenticate,
    get_all_users_json,
    get_all_staff_json,
    get_all_students_json,
    search_staff,
    create_notification,
    change_status,
    get_all_notifs_json,
    create_recommendation,
    get_all_recommendations_json
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    # test_new_student()
    def test_new_student(self):
        newstudent = Student("rob@mail.com", "pass", "student", "Rob", "Singh")
        assert newstudent.firstName == "Rob", newstudent.lastName == "Singh"
        assert newstudent.email == "rob@mail.com", newstudent.userType=="student"

    # test_new_staff()
    def test_new_staff(self):
        newstaff = Staff("bob@mail.com", "pass", "staff", "Bob", "Jones")
        assert newstaff.firstName == "Bob", newstaff.lastName == "Jones"
        assert newstaff.email == "bob@mail.com", newstaff.userType=="staff"

    # pure function no side effects or integrations called
    # test_student_toJSON()
    def test_student_toJSON(self):
        student = Student("rob@mail.com", "pass", "student", "Rob", "Singh")
        student_json = student.toJSON()
        self.assertDictEqual(student_json, {"studentID":None, "email":"rob@mail.com", "userType":"student", "firstName":"Rob","lastName":"Singh"})
    
    # test_staff_toJSON()
    def test_staff_toJSON(self):
        staff = Staff("bob@mail.com", "pass", "staff", "Bob", "Jones")
        staff_json = staff.toJSON()
        self.assertDictEqual(staff_json, {"staffID":None, "email":"bob@mail.com", "userType":"staff", "firstName":"Bob","lastName":"Jones"})
    
    # test_hashed_password()
    def test_hashed_password(self):
        password = "pass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob@mail.com", password, "staff", "Bob", "Jones")
        assert user.password != password

    #test_check_password()
    def test_check_password(self):
        password = "pass"
        user = User("bob@mail.com", password, "staff", "Bob", "Jones")
        assert user.check_password(password) != password
        
    #test_new_recommendation()
    def test_new_recommendation(self):
        newrec = Recommendation("1", "2", "www.link.com/recURL")
        assert newrec.sentFromStaffID=="1", newrec.sentToStudentID =="2"
        assert newrec.recURL =="www.link.com/recURL"

    #test_rec_toJSON()
    def test_rec_toJSON(self):
        rec = Recommendation("1", "2", "www.link.com/recURL")
        rec_json = rec.toJSON()
        self.assertDictEqual(rec_json, {"recID":None, "sentFromStaffID":"1", "sentToStudentID":"2", "recURL":"www.link.com/recURL"})   

    #test_new_notification()
    def test_new_notification(self):
        newnotif = Notification("1", "2", "Please send a recommendation to me")
        assert newnotif.sentToStaffID=="1", newnotif.sentFromStudentID =="2"
        assert newnotif.requestBody =="Please send a recommendation to me", newnotif.status =="unread"

    #test_notif_toJSON()
    def test_notif_toJSON(self):
        notif = Notification("1", "2", "Please send a recommendation to me")
        notif_json = notif.toJSON()
        self.assertDictEqual(notif_json, {"notifID":None, "sentToStaffID": "1", "sentFromStudentID":"2", "requestBody":"Please send a recommendation to me", "status":"unread"})


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

# test_authenticate()
def test_authenticate():
    user = create_user("bob@mail.com", "pass", "staff", "Bob", "Jones")
    try:
        db.session.add(user)
    except:
        db.session.rollback()
    assert authenticate(user.email,"pass") != None
    db.session.remove()

class UsersIntegrationTests(unittest.TestCase):

    # test_create_user()
    def test_create_user(self):
        user = create_user("rob@mail.com", "pass", "student", "Rob", "Singh")
        assert user.email == "rob@mail.com"
        
    # test_get_all_users_json()
    def test_get_all_users_json(self):
        user1 = create_user("bob@mail.com", "pass", "staff", "Bob", "Jones")
        db.session.add(user1)
        user2 = create_user("rob@mail.com", "pass", "student", "Rob", "Singh")   
        db.session.add(user2)
        
        users_json = get_all_users_json()
        
        db.session.remove()
        
        self.assertListEqual([{"id":1, "email":"bob@mail.com", "userType":"staff", "firstName":"Bob", "lastName":"Jones"},
                              {"id":2, "email":"rob@mail.com", "userType":"student", "firstName":"Rob", "lastName":"Singh"}],
                             users_json)
            
    # test_get_all_students_json()
    def test_get_all_students_json(self):
        user1 = create_user("bob@mail.com", "pass", "staff", "Bob", "Jones")
        user2 = create_user("rob@mail.com", "pass", "student", "Rob", "Singh")
        user3 = create_user("chloe@mail.com", "mypass", "student", "Chloe", "Smith")
        
        try:
            db.session.add(user1)
            db.session.add(user2)
            db.session.add(user3)
        except:
            db.session.rollback()
            
        students_json = get_all_students_json()
        
        self.assertListEqual([{"studentID":2, "email":"rob@mail.com", "userType":"student", "firstName":"Rob", "lastName":"Singh"},
                              {"studentID":3, "email":"chloe@mail.com", "userType":"student", "firstName":"Chloe", "lastName":"Smith"}],
                             students_json)
        db.session.remove()
        
    # test_get_all_staff_json()
    def test_get_all_staff_json(self):
        user1 = create_user("bob@mail.com", "pass", "staff", "Bob", "Jones")
        user2 = create_user("rob@mail.com", "pass", "student", "Rob", "Singh")
        user3 = create_user("j@mail.com", "mypass", "staff", "John", "Smith")
        
        try:
            db.session.add(user1)
            db.session.add(user2)
            db.session.add(user3)
        except:
            db.session.rollback()
            
        staff_json = get_all_staff_json()
        
        self.assertListEqual([{"staffID":1, "email":"bob@mail.com", "userType":"staff", "firstName":"Bob", "lastName":"Jones"},
                              {"staffID":3, "email":"j@mail.com", "userType":"staff", "firstName":"John", "lastName":"Smith"}],
                             staff_json)
        db.session.remove()
                
    # test_search_staff
    def test_search_staff(self):
        user1 = create_user("bob@mail.com", "pass", "staff", "Bob", "Jones")
        user2 = create_user("rob@mail.com", "pass", "student", "Rob", "Singh")
        user3 = create_user("j@mail.com", "mypass", "staff", "John", "Smith")
        
        try:
            db.session.add(user1)
            db.session.add(user2)
            db.session.add(user3)
        except:
            db.session.rollback()
            
        staff = search_staff("ID", "1")
        
        db.session.remove()
        
        self.assertDictEqual({"staffID":1, "email":"bob@mail.com", "userType":"staff", "firstName":"Bob", "lastName":"Jones"},
                             staff)
        
    
    # test_send_request
    def test_send_notification(self):
        staff = create_user("bob@mail.com", "pass", "staff", "Bob", "Jones")
        student = create_user("rob@mail.com", "pass", "student", "Rob", "Singh")
        
        try:
            db.session.add(staff)
            db.session.add(student)
        except:
            db.session.rollback
        
        notif = create_notification(staff.id, 2, "I need a recommendation")
        
        staff.notificationFeed.append(notif)
        db.session.remove()
                
        assert staff.notificationFeed != None
        
    
    # test_get_notification()
    def test_get_notification(self):
        staff = create_user("bob@mail.com", "pass", "staff", "Bob", "Jones")
        student = create_user("rob@mail.com", "pass", "student", "Rob", "Singh")
        
        try:
            db.session.add(staff)
            db.session.add(student)
        except:
            db.session.rollback
        
        notif = create_notification(1, 2, "I need a recommendation")
        db.session.add(notif)
        
        notif = Notification.query.get(1)
        db.session.remove()
        self.assertDictEqual({"notifID":1, "sentToStaffID": 1, "sentFromStudentID":2, "requestBody":"I need a recommendation", "status":"unread"},
                             notif.toJSON())
        
       
    # test_get_all_notifications_json()
    # def test_get_all_notifications_json(self):
        
    #     staff = create_user("bob@mail.com", "pass", "staff", "Bob", "Jones")
    #     student = create_user("rob@mail.com", "pass", "student", "Rob", "Singh")
        
    #     try:
    #         db.session.add(staff)
    #         db.session.add(student)
    #     except:
    #         db.session.rollback
        
    #     notif = create_notification(staff.id, 2, "I need a recommendation")
    #     db.session.add(notif)
    #     staff.notificationFeed.append(notif)
        
    #     notif = create_notification(staff.id, 2, "Please write me a recommendation")
    #     db.session.add(notif)
    #     staff.notificationFeed.append(notif)
        
    #     notifs_json = get_all_notifs_json()
        
    #     db.session.remove()
        
    #     self.assertListEqual([{"notifID":1, "sentToStaffID": 1, "sentFromStudentID":2, "requestBody":"I need a recommendation", "status":"unread"},
    #                           {"notifID":2, "sentToStaffID": 1, "sentFromStudentID":2, "requestBody":"Please write me a recommendation", "status":"unread"}],
    #                          notifs_json)
        
    
    # test_approve_request
    def test_approve_request(self):
        staff = create_user("bob@mail.com", "pass", "staff", "Bob", "Jones")
        student = create_user("rob@mail.com", "pass", "student", "Rob", "Singh")
        
        try:
            db.session.add(staff)
            db.session.add(student)
        except:
            db.session.rollback
        
        notif = create_notification(1, 2, "I need a recommendation")
        db.session.add(notif)
        staff.notificationFeed.append(notif)
        
        notif = change_status(notif, "approved")
        
        db.session.remove()
        
        self.assertDictEqual({"notifID":None, "sentToStaffID": 1, "sentFromStudentID":2, "requestBody":"I need a recommendation", "status":"approved"},
                                notif.toJSON())
        

    # test_send_recommendation
    def test_send_recommendation(self):
        staff = create_user("bob@mail.com", "pass", "staff", "Bob", "Jones")
        student = create_user("rob@mail.com", "pass", "student", "Rob", "Singh")
        
        try:
            db.session.add(staff)
            db.session.add(student)
        except:
            db.session.rollback
    
        newrec = create_recommendation(staff.staffID, student.studentID, "www.link.com/link")
        student.recommendationList.append(newrec)
        
        db.session.remove()
        
        assert student.recommendationList != None
  
    
    # test_get_recommendation()
    def test_get_notification(self):
        staff = create_user("bob@mail.com", "pass", "staff", "Bob", "Jones")
        student = create_user("rob@mail.com", "pass", "student", "Rob", "Singh")
        
        try:
            db.session.add(staff)
            db.session.add(student)
        except:
            db.session.rollback
        
        newrec = create_recommendation(1, 2, "www.link.com/link")
        student.recommendationList.append(newrec)
        db.session.add(newrec)
        
        newrec = Recommendation.query.get(1)
        db.session.remove()
        self.assertDictEqual({"recID":1, "sentFromStaffID": 1, "sentToStudentID":2, "recURL":"www.link.com/link"},
                             newrec.toJSON())
        
        
    # test_get_all_recommendations_json()
    def test_get_all_recommendations_json(self):
        staff = create_user("bob@mail.com", "pass", "staff", "Bob", "Jones")
        student = create_user("rob@mail.com", "pass", "student", "Rob", "Singh")
        
        try:
            db.session.add(staff)
            db.session.add(student)
        except:
            db.session.rollback
        
        newrec = create_recommendation(1, 2, "www.link.com/link")
        student.recommendationList.append(newrec)
        db.session.add(newrec)
        
        newrec = create_recommendation(1, 2, "www.newlink.com/link2")
        student.recommendationList.append(newrec)
        db.session.add(newrec)
        
        recs_json = get_all_recommendations_json()
        
        db.session.remove()
        
        self.assertListEqual([{"recID":1, "sentFromStaffID": 1, "sentToStudentID":2, "recURL":"www.link.com/link"},
                              {"recID":2, "sentFromStaffID": 1, "sentToStudentID":2, "recURL":"www.newlink.com/link2"}],
                             recs_json)
    