from App.models import Notification
from App.database import db
from sqlalchemy.exc import IntegrityError
from App.controllers import get_staff

#accept request (pending) objects and create a notification for it
def create_notifications(requests, staff):
    for request in requests:
        newNotif = Notification(staffId=request.staffId, requestID=request.requestID, body=request.body, dateNTime=request.dateNTime, seen=False)
        if newNotif:
            db.session.add(newNotif)
            db.session.commit()
    notificans = get_all_notifs(staff)
    return notications


#get all unseen notifications for a staff member
def get_all_notifs(staff):
    return Notification.query.all(staffid=staff.id, seen=false)


#get a notification by id
def get_notif(notifID):
    return Notification.query.filter_by(notifID=notifID).first()


# def send_notification(sentFromStudentID, requestBody, sentToStaffID):
#     # get staff feed - notif list
#     staff = get_staff(sentToStaffID)
#     # new notif
#     newNotif = create_notification(sentToStaffID, sentFromStudentID, requestBody)
#     try:
#         db.session.add(newNotif)
#         db.session.commit()
#     except IntegrityError:
#         db.session.rollback()
#         return None
#     # add notif to list
#     staff.notificationFeed.append(newNotif)
#     try:
#         db.session.add(staff)
#         db.session.commit()
#     except IntegrityError:
#         db.session.rollback()
#         return None
#     return staff



# def get_all_notifs_json():
#     notifs = get_all_notifs()
#     if not notifs:
#         return None
#     notifs = [notif.toJSON() for notif in notifs]
#     return notifs

# # gets a notification from a user's notif feed
# #search notification by Notification ID
# def get_user_notif(staffID, notifID):
#     return Notification.query.filter_by(sentToStaffID=staffID, notifID=notifID).first()





# def change_status(notif, status):
#     if notif:
#         notif.status = true
#         return notif
#     return None


'''
# approve notif
def approve_notif(staffID, notifID, status):
    notif = get_user_notif(staffID, notifID)
    notif = change_status(notif, status)
    if notif:
        try:
            db.session.add(notif)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return None
    return notif
'''