from App.database import db
import enum

Class Status(enum.Enum):
 ACCEPTED = "Accepted"
 REJECTED = "Rejected"
 PENDING = "Pending"

class Request(db.Model):
    requestID = db.Column(db.Integer, primary_key=True)
    staffId = db.Column(db.Integer,db.ForeignKey('staff.staffId'))
    studentId = db.Column(db.Integer,db.ForeignKey('student.studentId'))
    body = db.Column(db.String, nullable=False)
    status = db.Column(db.Enum(Status), nullable = False, default = status.PENDING)
    dateNTime = db.Column(db.TIMESTAMP,nullable=False)
    deadline = db.Column(db.Date, nullable=False)

    def __init__(self, requestId, staffId, studentId, body, dateNTime, deadline):
        self.requestID = requestID
        self.staffId = staffId
        self.studentId = studentId
        self.body = body
        self.status = status
        self.dateNTime = dateNTime
        self.deadline = deadline
        
    def toJSON(self):
        return{
            'notifId': self.notifId,
            'staffId': self.staffId,
            'requestID': self.requestID,
            'body': self.body,
            'status': self.status,
            'dateNTime': self.dateNTime,
            'seen': self.seen
        }