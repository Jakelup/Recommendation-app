from App.models import Request
from App.database import db

#TO DO:

def get_all_student_requests():
    return Request.query.all()


def get_all_student_requests_JSON():
    requests = get_all_student_requests()
    if not requests:
        return None
    requests = [requests.toJSON() for requests in requests]
    return requests

def get_request():
    return 0
    
def get_request_JSON():
    return 0
    
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