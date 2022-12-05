from App.models import Staff, Recommendation, Notification
from App.database import db
from flask import jsonify


# STAFF SIGNUP
def create_staff(id, username, password, name, faculty, department):
    newStaff = Staff(id=id, username=username, password=password, name=name, faculty=faculty, department=department)
    # db.session.add(newStaff)
    # db.session.commit()
    # return newStaff
    try:
        db.session.add(newStaff)
        db.session.commit()
        return newStaff
    except IntegrityError: # attempted to insert a duplicate user or other errors
        db.session.rollback()
        return None



###Staff Info Functions
#search staff by ID
def get_staff(id):
    staff=Staff.query.get(id)
    if staff:
        return staff
    return None

def get_all_staff():
    return Staff.query.all()

def get_all_staff_json():
    staff = get_all_staff()
    if not staff:
        return None
    staff_json = [staff.toJSON() for staf in staff]
    return staff_json

def get_all_staff_notifs_json():
    staff = get_all_staff()
    if not staff:
        return None
    staff = [staf.toJSON_with_notifications() for staf in staff]
    return staff

#get the staff object for the recommendation
def get_staff_by_recommendation(recommendation):
    staff=Staff.query.get(id=recommendation.staffId)
    if staff:
        return staff
    return None


# def get_staff_by_firstName(firstName):
#     staff= Staff.query.filter_by(firstName=firstName).all()
#     staff = [staf.toJSON() for staf in staff]
#     if staff==[]:
#         return None
#     return jsonify(staff)

# def get_staff_by_lastName(lastName):
#     staff=Staff.query.filter_by(lastName=lastName).all()
#     staff = [staf.toJSON() for staf in staff]
#     if staff == []:
#         return None
#     return jsonify(staff)

def get_staff_by_name(name):
    staff=Staff.query.filter_by(name=name).all()
    staff = [staf.toJSON() for staf in staff]
    if staff == []:
        return None
    return staff

# def search_staff(type, keyword):
#     if (type=="ID"):
#         staff = get_staff(keyword)
#         return staff.toJSON()
#     else:
#         if (type=="name"):
#             name=keyword.split(",")
#             return get_staff_by_name(name[0], name[1])
#         if (type=="firstName"):
#             return get_staff_by_firstName(keyword)
#         if (type=="lastName"):
#             return get_staff_by_lastName(keyword)
#     return None


### Notification Functions
def get_staff_feed(staffID):
    staff = get_staff(staffID)
    return staff.notificationList

# get the notification feed for the current user
def get_staff_feed_json(staffID):
    notifs = get_staff_feed(staffID)
    if notifs:
        return [notif.toJSON() for notif in notifs]
   


### Recommendation Functions
'''
def accept_request(requestId):
    update_status(requestId,"accepted")
    return None

def reject_request(requestId):
    update_status(requestId,"rejected")
    return None
    '''
'''
def create_recommendation(sentFromStaffID, sentToStudentID, recURL):
    newrec = Recommendation(sentFromStaffID=sentFromStaffID, sentToStudentID=sentToStudentID, recURL=recURL)
    return newrec'''

##This function should be used for staff submitting rec. Considering moving to views. Will review in testing
def submit_recommendation(sentFromStaffID, sentToStudentID, recURL):
    student = Student.query.get(sentToStudentID)
    newrec = create_recommendation(sentFromStaffID, sentToStudentID, recURL)
    try:
        db.session.add(newrec)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return None
    student.recommendationList.append(newrec)
    try:
        db.session.add(student)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return None
    return student
