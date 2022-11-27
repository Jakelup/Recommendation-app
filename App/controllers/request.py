from App.models import Request
from App.database import db

#TO DO:

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
    
def get_pendingR_byStud():
    return 0

def get_acceptedR_byStud():
    return 0

def get_acceptedR_byStaff():
    return 0

def get_rejectedR_byStaff():
    return 0

def get_completedR_byStaff():
    return 0

def get_pendingR_byStaff():
    return 0