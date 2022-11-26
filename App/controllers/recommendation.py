from App.models import Recommendation, Student
from App.database import db
from sqlalchemy.exc import IntegrityError


def create_recommendation(sentFromStaffID, sentToStudentID, recURL):
    newrec = Recommendation(sentFromStaffID=sentFromStaffID, sentToStudentID=sentToStudentID, recURL=recURL)
    return newrec
    
def get_all_recommendations():
    return Recommendation.query.all()

def get_all_recommendations_json():
    recs = get_all_recommendations()
    if not recs:
        return None
    recs = [rec.toJSON() for rec in recs]
    return recs

def get_recommendation(studentID, recID):
    rec = Recommendation.query.filter_by(sentToStudentID=studentID, recID=recID).first()
    if rec:
        return rec.toJSON()
    return None



