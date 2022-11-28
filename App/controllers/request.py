from App.models import Request
from App.database import db


def get_all_student_requests(studentId):
    return Request.query.filter_by(studentId).first()

def get_all_student_requests_JSON(studentId):
    requests = get_all_student_requests(studentId)
    if not requests:
        return None
    requests = [request.toJSON() for request in requests]
    return requests



def get_all_staff_requests(staffId):
    return Request.query.filter_by(staffId).first()

def get_all_staff_request_JSON(staffId):
    requests = get_all_student_requests(staffId)
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

#CHANGE REQUEST STATUS
def change_status(requestID):


    return 0


#STUDENT REQUESTS
def get_student_pendingR(studentId):
    requests = get_all_student_requests(studentId)
    if not requests:
        return None
    requests = Request.query.filter_by(Status="Pending").all()
    return requests

def get_student_acceptedR(studentId):
    requests = get_all_student_requests(studentId)
    if not requests:
        return None
    requests = Request.query.filter_by(Status="Accepted").all()
    return requests



##STAFF REQUESTS
def get_staff_acceptedR(staffId):
    requests = get_all_staff_requests(staffId)
    if not requests:
        return None
    requests = Request.query.filter_by(Status="Accepted").all()
    return requests

def get_staff_rejectedR(staffId):
    requests = get_all_staff_requests(staffId)
    if not requests:
        return None
    requests = Request.query.filter_by(Status="Rejected").all()
    return requests

def get_staff_completedR():
    requests = get_all_staff_requests(staffId)
    if not requests:
        return None
    requests = Request.query.filter_by(Status="Completed").all()
    return requests

def get_staff_pendingR():
    requests = get_all_staff_requests(staffId)
    if not requests:
        return None
    requests = Request.query.filter_by(Status="Pending").all()
    return requests