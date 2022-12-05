from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response
from flask_jwt import jwt_required, current_identity
from flask_login import login_required, current_user

from App.controllers import (
    get_staff, 
    get_all_staff,
    get_all_staff_json,
    get_all_staff_notifs_json,
    get_staff_by_name,
    get_staff_feed_json,
    get_staff_acceptedR,
    get_staff_completedR,
    get_staff_rejectedR,
    create_notification,
    get_all_notifs_unseen
)

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')



## Render first version of staffMain.html
@staff_views.route('/staffMain', methods=['GET'])
@login_required 
def staffMain():
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


   



# VIEW NOTIFICATION FEED
@staff_views.route('/notifications', methods=['GET'])
@login_required 
@jwt_required()
def view_user_feed():
    staffID = current_identity.id
    if get_staff(staffID):
        notifs = get_staff_feed_json(staffID)
        if notifs:
            return jsonify(notifs)
        return Response('no notifications found for this user', status=404)
    return Response({"students cannot perform this action"}, status=401)


# routes for testing purposes
@staff_views.route('/view/staff', methods=['GET'])
@login_required 
def get_staff_page():
    staff = get_all_staff()
    return render_template('users.html', users=staff)

# JSON view all Staff
@staff_views.route('/staff', methods=['GET'])
@login_required 
def staff():
    staff = get_all_staff_json()
    if staff:
        return jsonify(staff)
    return ("No staff users recorded")



# JSON view all staff + their notification feed
@staff_views.route('/staff/NotifFeed', methods=['GET'])
@login_required 
def staff_notifs():
    staff = get_all_staff_notifs_json()
    if staff:
        return jsonify(staff)