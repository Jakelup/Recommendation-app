from App.database import db
import enum

class Status(enum.Enum):
 ACCEPTED = "Accepted"
 REJECTED = "Rejected"
 PENDING = "Pending"
 COMPLETED = "Completed"

class Request(db.Model):
    requestID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staffId = db.Column(db.Integer,db.ForeignKey('staff.id'))
    studentId = db.Column(db.Integer,db.ForeignKey('student.id'))
    body = db.Column(db.String, nullable=False)
    status = db.Column(db.Enum(Status), nullable = False, default = Status.PENDING)
    dateNTime = db.Column(db.TIMESTAMP,nullable=False)
    # deadline = db.Column(db.Date, nullable=False)

    def __init__(self, staffId, studentId, body, dateNTime, status):
        self.staffId = staffId
        self.studentId = studentId
        self.body = body
        self.status = status
        self.dateNTime = dateNTime
        # self.deadline = deadline
        
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