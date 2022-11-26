from App.database import db

class Recommendation(db.Model):
    recId = db.Column(db.Integer, primary_key=True)
    staffId = db.Column(db.Integer, db.ForeignKey('staff.staffId'))
    studentId = db.Column(db.Integer, db.ForeignKey('student.studentId'))
    body = db.Column(db.String, nullable=False)
    date = db.Coloumn(db.date, nullable= False)

    def __init__(self, staffId,studentId, body):
        self.staffId = staffId
        self.studentId=studentId
        self.body=body
    
    def toJSON(self):
        return{
            'studentId': self.studentId,
            'staffId': self.staffId,
            'studentId': self.studentId,
            'body': self.body
        }

    
