from App.database import db

class Notification(db.Model):
    notifId = db.Column(db.Integer, primary_key=True)
    # who it was sent to
    staffid = db.Column(db.Integer,db.ForeignKey('staff.id'))
    # who sent it
    requestId = db.Column(db.Integer, db.ForeignKey('request.requestID'))
    body = db.Column(db.String, nullable=False)
    dateNTime = db.Column(db.TIMESTAMP, nullable=False)
    seen = db.Column(db.Boolean, default=False, nullable=False)
    

    def __init__(self, notifId, staffId, requestID, body, dateNTime, seen):
        self.notifId = notifId
        self.staff = staffid
        self.requestId =requestId
        self.body = body
        self.dateNTime = dateNTime
        self.seen = seen
        
    def toJSON(self):
        return{
            'notifId': self.notifId,
            'staffId': self.staffid,
            'requestID': self.requestID,
            'body': self.body,
            'dateNTime': self.dateNTime,
            'seen': self.seen
        }