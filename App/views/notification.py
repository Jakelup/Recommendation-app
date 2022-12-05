from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response, redirect, url_for
from flask_jwt import jwt_required, current_identity
from flask_login import login_required, current_user
from App.models import Status

from App.controllers import (
    get_staff,
    get_notif,
    get_request,
    change_status,
    get_staff_acceptedR,
    get_staff_completedR,
    get_staff_rejectedR,
    get_all_notifs_unseen,
    # approve_notif, REMOVED DURING REFACTORING OF NOTICATION CONTROLLER
    get_staff_pendingR
)

notification_views = Blueprint('notification_views', __name__, template_folder='../templates')


## REJECT
@notification_views.route('/staffMain/reject', methods=['GET','POST'])
@login_required
def requestRejected():
    # data = request.form
    notification = get_notif(request.form.get('notifid'))
    
    if notification:
        therequest = get_request(notification.requestId) #find the original request

        if therequest: 
        #change the status of that request
            therequest = change_status(therequest.requestID, Status.REJECTED)
        notification.seen = True
    
    staffID = current_user.id
    staff = get_staff(staffID)

    ##get accepted requests
    acceptedrs = get_staff_acceptedR(staffID)
        
    ##get rejected and completed requests
    completedrs = get_staff_completedR(staffID)
    rejectedrs = get_staff_rejectedR(staffID)

    ##get all notifications
    notifications = get_all_notifs_unseen(staff)
    return render_template('staffMain.html', staff=staff, completedrs=completedrs, rejectedrs=rejectedrs, acceptedrs=acceptedrs, selectedRec=0, notifications=notifications)




##ACCEPT NOTIFICATION
@notification_views.route('/staffMain/accept', methods=['GET','POST'])
@login_required
def requestAccepted():
    # data = request.form
    notification = get_notif(request.form.get('notifid'))
    
    if notification:
        therequest = get_request(notification.requestId) #find the original request

        if therequest: 
        #change the status of that request
            therequest = change_status(therequest.requestID, Status.ACCEPTED)
        notification.seen = True
    
    staffID = current_user.id
    staff = get_staff(staffID)

    ##get accepted requests
    acceptedrs = get_staff_acceptedR(staffID)
        
    ##get rejected and completed requests
    completedrs = get_staff_completedR(staffID)
    rejectedrs = get_staff_rejectedR(staffID)

    ##get all notifications
    notifications = get_all_notifs_unseen(staff)
    return render_template('staffMain.html', staff=staff, completedrs=completedrs, rejectedrs=rejectedrs, acceptedrs=acceptedrs, selectedRec=0, notifications=notifications)

















'''
# SEND REQUEST TO STAFF MEMBER
@notification_views.route('/request/send', methods=['POST'])
@jwt_required()
def sendRequest():
    if not get_staff(current_identity.id):
        data = request.get_json()
        staff = get_staff(data['sentToStaffID'])
        if not staff:
            return Response({'staff member not found'}, status=404)
        send_notification(current_identity.id, data['requestBody'], data['sentToStaffID'])
        return Response({'request sent successfully'}, status=200)
    return Response({"staff cannot perform this action"}, status=401)

'''

# SEND NOTIFICATIONS TO NOTIFICATIONLOG.HTML


'''## Old thought process: (ignore and try checklist items on trello task first)""
#Create route with address /staffMain/notifcationLog/<staffID> to get and return notifcations 
#(created from pendings requests for a staff: Refactor routes below to interact with request object)

#Create route /staffMain/acceptRequest/<reqID> that will change the status of a request to accepted. Change the notification to seen using the ID
#Seen notifications should no longer have accept reject buttons
#(Use change_status(reqID, "Accepted"), it's already imported)

#Create route /staffMain/acceptRequest/<reqID> that will change the status of a request to rejected. Change the notification to seen using the ID
#Seen notifications should no longer have accept reject buttons
#(Use change_status(reqID, "Rejected"), it's already imported)'''







### ARCHIVE- ORIGINAL CODE: 

# SEND NOTIFICATION TO STAFF MEMBER
@notification_views.route('/request/send', methods=['POST'])
@jwt_required()
def notify_staff(notifId):
    if get_staff(current_identity.id):
        data = get_request()
        staff = get_staff(data['sentToStaffID'])
        if not staff:
            return Response({'staff member not found'}, status=404)
        send_notification(current_identity.id, data['requestBody'], data['sentToStaffID'])
    return None   


# VIEW NOTIFICATION
@notification_views.route('/notifications/<notifID>', methods=['GET'])
@jwt_required()
def view_notif(notifID):
    staff = get_staff(current_identity.id)
    if staff:
        if not staff.notificationFeed:
            return Response({"no notifications found for this user"}, status=404)
        notif = get_user_notif(current_identity.id, notifID)
        if notif:
            return jsonify(notif.toJSON())
        return Response({"notification with id " + notifID + " not found"}, status=404)
    return Response({"students cannot perform this action"}, status=401)


# APPROVE REQUEST
@notification_views.route('/request/<notifID>', methods=['POST'])
@jwt_required()
def approve_request(notifID):
    status = request.get_json()
    staff = get_staff(current_identity.id)
    if staff:
        notif = approve_notif(staff.id, notifID, status['status'])
        if notif:
            return Response({"request " + status['status']}, status=200)
        return Response({"invalid request"}, status=401)
    return Response({"students cannot perform this action"}, status=401)


# Routes for testing purposes
# get all notification objects
@notification_views.route('/notifs', methods=['GET'])
def get_all_notifications():
    notifs = get_all_notifs_json()
    return jsonify(notifs)