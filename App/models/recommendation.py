from App.database import db
from datetime import date

class Recommendation(db.Model):
    recId = db.Column(db.Integer, primary_key=True)
    staffId = db.Column(db.Integer, db.ForeignKey('staff.id'))
    studentId = db.Column(db.Integer, db.ForeignKey('student.id'))
    body = db.Column(db.String, nullable=False)
    date = db.Column(db.TIMESTAMP,nullable=False)


    def __init__(self, staffId, studentId, body, date):
        self.staffId = staffId
        self.studentId=studentId
        self.body=body
        self.date = date
    
    def toJSON(self):
        return{
            'recId': self.recId,
            'staffId': self.staffId,
            'studentId': self.studentId,
            'body': self.body,
            'date': self.date
        }

    
