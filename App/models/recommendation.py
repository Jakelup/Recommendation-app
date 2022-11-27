from App.database import db

class Recommendation(db.Model):
    recId = db.Column(db.Integer, primary_key=True)
    staffId = db.Column(db.Integer, db.ForeignKey('staff.staffId'))
    studentId = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    body = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable= False)

    def __init__(self, recId, staffId, studentId, body, date):
        self.recId = recId
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

    
