from App.database import db
from App.models import User, user


class Student(User):
    __tablename__ = 'student'
    # student has a list of recommendation objects
    recommendationList = db.relationship('Recommendation', backref=db.backref('student', lazy='joined'))
    requests = db.relationship('Request',  backref=db.backref('student', lazy='joined')) 

    __mapper_args__ = {
        "polymorphic_identity": "student",
    }

    def __init__(self, id, username, password, name, faculty, department):
        self.username = username
        self.set_password(password)
        self.name = name
        self.faculty = faculty
        self.department = department
        self.id = id
        self.userType = "staff"



    def toJSON(self):
        return{
            'studentId': self.id,
            'name': self.name,
            'faculty': self.faculty,
            'department': self.department
        }
        
    def toJSON_with_recommendations(self):
        return{
            'studentId': self.id,
            'name': self.name,
            'faculty': self.faculty,
            'department': self.department,
            'recommendationList': [recommendation.toJSON() for recommendation in self.recommendationList]
        }

