from App.models import Request
from App.database import db
from datetime import date


def create_request(studentId, staffId, body):
    ### request ID auto generated???
    datetime = date.today()
    # deadline = date.today() + timedelta(days=10)# temp measure until buttons have been decided
    request = Request(staffId=staffId, studentId=studentId, body=body, dateNTime=datetime)
    if request:
        db.session.add(request)
        db.session.commit()
        return request
    return None

def get_all_student_requests(studentId):
    return Request.query.filter_by(studentId=studentId).first()

def get_all_student_requests_JSON(studentId):
    requests = get_all_student_requests(studentId)
    if not requests:
        return None
    requests = [request.toJSON() for request in requests]
    return requests



def get_all_staff_requests(staffId):
    return Request.query.filter_by(staffId=staffId).first()

def get_all_staff_request_JSON(staffId):
    requests = get_all_student_requests(staffId=staffId)
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
def change_status(requestID,newStatus):
    request = get_request(requestID)
    request.Status = newStatus
    return request


#STUDENT REQUESTS
def get_student_pendingR(studentId):
    requests = get_all_student_requests(studentId)
    if not requests:
        return None
    requests = Request.query.filter(Request.status.in_(Status.PENDING)).all()
    return requests

def get_student_acceptedR(studentId):
    requests = get_all_student_requests(studentId)
    if not requests:
        return None
    requests = Request.query.filter(Request.status.in_(Status.ACCEPTED)).all()
    return requests



##STAFF REQUESTS
def get_staff_acceptedR(staffId):
    requests = get_all_staff_requests(staffId)
    if not requests:
        return None
    requests = Request.query.filter_by(Request.status.in_(Status.ACCEPTED)).all()
    return requests

def get_staff_historyR(staffId):
    requests = get_all_staff_requests(staffId)
    if not requests:
        return None
    requests = Request.query.filter_by(Request.status.in_([Status.REJECTED, Status.COMPLETED])).all()
    return requests



#staff does not handle pending requests directly, they are turned into notifications. notification.py uses this:
def get_staff_pendingR():
    requests = get_all_staff_requests(staffId)
    if not requests:
        return None
    requests = Request.query.filter_by(Request.status.in_(Status.PENDING)).all()
    return requests