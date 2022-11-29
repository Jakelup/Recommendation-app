from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response
from flask_jwt import jwt_required, current_identity
from flask_login import login_required, current_user

from App.controllers import (
    get_staff, 
    get_all_staff,
    get_all_staff_json,
    get_all_staff_notifs_json,
    get_staff_by_name,
    get_staff_feed_json
)

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')


## Render first version of staffMain.html
@staff_views.route('/staffMain', methods=['GET'])
# @login_required -- enable this once login is set up
def load_page():
    return render_template('staffMain.html')











    

### ARCHIVE- ORIGINAL CODE: 

# VIEW NOTIFICATION FEED
@staff_views.route('/notifications', methods=['GET'])
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
def get_staff_page():
    staff = get_all_staff()
    return render_template('users.html', users=staff)

# JSON view all Staff
@staff_views.route('/staff', methods=['GET'])
def staff():
    staff = get_all_staff_json()
    if staff:
        return jsonify(staff)
    return ("No staff users recorded")



# JSON view all staff + their notification feed
@staff_views.route('/staff/NotifFeed', methods=['GET'])
def staff_notifs():
    staff = get_all_staff_notifs_json()
    if staff:
        return jsonify(staff)