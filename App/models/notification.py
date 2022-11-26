from App.database import db

class Notification(db.Model):
    notifId = db.Column(db.Integer, primary_key=True)
    # who it was sent to
    staffId= db.Coloumn(db.Integer,db.ForeignKey('staff.staffId'))
    # who sent it
    # requestId = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    body = db.Column(db.String, nullable=False)
    seen = db.Column(db.Boolean,default=False nullable=False)

    def __init__(self, staffId,studentId, body):
        self.staffId = staffId
        # self.requestId=requestId
        self.body=body
        self.seen=seen
        
    def toJSON(self):
        return{
            'notifId': self.notifId,
            'staffId': self.staffId,
            # 'requestID': self.requestID,
            'body': self.body,
            'seen': self.seen
        }