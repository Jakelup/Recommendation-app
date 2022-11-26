from App.database import db
from App.models import User

class Staff(User):
    staffId = db.Column(db.Integer, primary_key=True)
    # staff has a list of notification objects
    notificationList = db.relationship('Notification', backref=db.backref('staff', lazy='joined'))
    
    def toJSON(self):
        return {
            'staffId': self.staffId,
            'username': self.username,
            'name': self.name,
        }
    
    def toJSON_with_notifications(self):
        return {
            'staffId': self.staffId,
            'username': self.username,
            'name': self.name,
            'notificationList': [notif.toJSON() for notif in self.notificationList]
        }