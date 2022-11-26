from App.database import db
from App.models import User

class Student(User):
    studentId = db.Column(db.Integer, primary_key=True)
    # student has a list of recommendation objects
    recommendationList = db.relationship('Recommendation', backref=db.backref('student', lazy='joined'))
    
    def toJSON(self):
        return{
            'studentId': self.studentId,
            'username': self.username,
            'name': self.firstName,
            
        }
        
    def toJSON_with_recommendations(self):
        return{
            'staffId': self.staffId,
            'username': self.username,
            'name': self.name,
            'recommendationList': [recommendation.toJSON() for recommendation in self.recommendationList]
        }