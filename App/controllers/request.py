from App.models import Request
from App.database import db


def get_all_student_requests():
    return Request.query.all()


def get_all_student_requests_JSON():
    requests = get_all_student_requests()
    if not requests:
        return None
    requests = [request.toJSON() for request in requests]
    return requests

def get_request(requestID):
    return Request.query.filter_by(requestID).first()
    
def get_request_JSON(requestID):
    req = get_request(requestID)
    if not req:
        return None
    req = request.toJSON(req)
    return req
    


#STUDENT REQUESTS
def get_student_pendingR(studentID, requestID):
    req = get_request(requestID)
    #CHECK REQ STATUS FOR PENDING
    return 0

def get_student_acceptedR():
    return 0



##STAFF REQUESTS
def get_staff_acceptedR():
    return 0

def get_staff_rejectedR():
    return 0

def get_staff_completedR():
    return 0

def get_staff_pendingR():
    return 0