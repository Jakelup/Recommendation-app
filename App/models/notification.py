from App.database import db

class Notification(db.Model):
    notifId = db.Column(db.Integer, primary_key=True)
    # who it was sent to
    staffId= db.Column(db.Integer,db.ForeignKey('staff.staffId'))
    # who sent it
    requestId = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    body = db.Column(db.String, nullable=False)
    dateNTime = db.Column(db.TIMESTAMP, nullable=False)
    seen = db.Column(db.Boolean, default=False, nullable=False)
    

    def __init__(self, notifId, staffId, requestID, body, dateNTime, seen):
        self.notifId = notifId
        self.staffId = staffId
        self.requestId =requestId
        self.body = body
        self.dateNTime = dateNTime
        self.seen = seen
        
    def toJSON(self):
        return{
            'notifId': self.notifId,
            'staffId': self.staffId,
            'requestID': self.requestID,
            'body': self.body,
            'dateNTime': self.dateNTime,
            'seen': self.seen
        }