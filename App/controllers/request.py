from App.models import Request, Status
from App.database import db
from datetime import datetime


def create_request(studentId, staffId, body):
    ### request ID auto generated???
    date = datetime.now()
    # deadline = date.today() + timedelta(days=10)# temp measure until buttons have been decided
    request = Request(staffId=staffId, studentId=studentId, body=body, dateNTime=date, status=Status.PENDING)
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
    return Request.query.filter_by(requestID=requestID).first()
    
def get_request_JSON(requestID):
    req = get_request(requestID)
    if not req:
        return None
    req = request.toJSON(req)
    return req

#CHANGE REQUEST STATUS
def change_status(requestID,newStatus):
    request = get_request(requestID)
    request.status = newStatus
    return request


#STUDENT REQUESTS
def get_student_pendingR(studentId):
    queries = [Request.studentId==studentId]
    queries += [Request.status==Status.PENDING]
    requests = Request.query.filter(*queries).all()
    if requests:
        return requests
    return None

def get_student_acceptedR(studentId):
    queries = [Request.studentId==studentId]
    queries += [Request.status==Status.ACCEPTED]
    requests = Request.query.filter(*queries).all()
    if requests:
        return requests
    return None


##STAFF REQUESTS
def get_staff_acceptedR(staffId):
    queries = [Request.staffId==staffId]
    queries += [Request.status==Status.ACCEPTED]
    requests = Request.query.filter(*queries).all()
    if requests:
        return requests
    return None


# def get_staff_historyR(staffId):
#     #where request status is rejected & also completed
#     queries = [Request.staffId==staffId] 
#     queries += [Request.status==Status.COMPLETED]
#     # queries += [Request.status==Status.REJECTED] 
#     # doesnt work for a third filter
#     requests = Request.query.filter(*queries).all()
#     if requests:
#         return requests
#     return None


def get_staff_completedR(staffId):
    queries = [Request.staffId==staffId] 
    queries += [Request.status==Status.COMPLETED]
    requests = Request.query.filter(*queries).all()
    if requests:
        return requests
    return None


def get_staff_rejectedR(staffId):
    queries = [Request.staffId==staffId] 
    queries += [Request.status==Status.REJECTED]
    requests = Request.query.filter(*queries).all()
    if requests:
        return requests
    return None



#staff does not handle pending requests directly, they are turned into notifications. notification.py uses this:
def get_staff_pendingR(staffId):
    queries = [Request.staffId==staffId]
    queries += [Request.status==Status.PENDING]
    requests = Request.query.filter(*queries).all()
    if requests:
        return requests
    return None

