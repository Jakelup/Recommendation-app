from App.database import db
from App.models import User

class Staff(User):
    staffId = db.Column(db.Integer, primary_key=True)
    # staff has a list of notification objects
    notificationList = db.relationship('Notification', backref=db.backref('staff', lazy='joined'))
    # staff has a list of request objects
    requestList = db.relationship('Request', backref=db.backref('staff', lazy='joined'))
    

    def __init__(self, username, password, faculty, department, staffId, requestList):
        self.username = username
        self.set_password(password)
        self.name = name
        self.faculty = faculty
        self.department = department
        self.staffId = staffId
        self.requestList = requestList
        self.user_type = "staff"

    def toJSON(self):
        return {
            'staffId': self.staffId,
            'name': self.name,
            'faculty': self.faculty,
            'department': self.department
        }
    
    def toJSON_with_notifications(self):
        return {
            'staffId': self.staffId,
            'name': self.name,
            'faculty': self.faculty,
            'department': self.department,
            'notificationList': [notif.toJSON() for notif in self.notificationList]
        }