from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    get_all_student_requests,
    get_all_student_requests_JSON,
    get_request,
    get_request_JSON,
    change_status,
    get_student_pendingR,
    get_student_acceptedR,
    get_staff_acceptedR,
    get_staff_rejectedR,
    get_staff_completedR,
    get_staff_pendingR,
    create_request
)

request_views = Blueprint('request_views', __name__, template_folder='../templates')

## Create Route called /studentMain to:
# GET ALL PENDING REQUESTS
@request_views.route('/studentMain', methods=['GET'])
def view_all_pending_reqs():
    studentID = current_identity.id
    if get_student(studentID):
        pending = get_student_pendingR(studentID)
        if pending:
            return render_template('staffMain.html', pending=pendingRequests)
        return Response({'There are no pending requests found for this user.'}, status=404)
    return Response("Staff cannot perform this action.", status=401)

# GET ALL ACCEPTED REQUESTS
@request_views.route('/studentMain', methods=['GET'])
def view_all_accepted_reqs():
    studentID = current_identity.id
    if get_student(studentID):
        accepted = get_student_acceptedR(studentID)
        if accepted:
            return render_template('studentMain.html', accepted=acceptedRequests)
        return Response({'There are no accepted requests found for this user.'}, status=404)
    return Response("Staff cannot perform this action.", status=401)


## Create Route called /staffMain to: 
    #GET ALL ACCEPTED REQUESTS BY STAFF ID
    #BUILD HISTORY: GET ALL REJECTED AND COMPLETED REQUESTS BY STAFF ID
    
# GET ALL PENDING REQUESTS
@request_views.route('/staffMain', methods=['GET'])
def view_all_pending_reqs():
    staffID = current_identity.id
    if get_staff(staffID):
        pending = get_staff_pendingR(staffID)
        if pending:
            return render_template('staffMain.html', pending=pendingRequests)
        return Response({'There are no pending requests found for this user.'}, status=404)
    return Response("Student cannot perform this action.", status=401)

# GET ALL ACCEPTED REQUESTS
@request_views.route('/staffMain', methods=['GET'])
def view_all_accepted_reqs():
    staffID = current_identity.id
    if get_staff(staffID):
        accepted = get_staff_acceptedR(staffID)
        if accepted:
            return render_template('staffMain.html', accepted=acceptedRequests)
        return Response({'There are no accepted requests found for this user.'}, status=404)
    return Response("Students cannot perform this action.", status=401)

# GET ALL REJECTED REQUESTS
@request_views.route('/staffMain', methods=['GET'])
def view_all_rejected_reqs():
    staffID = current_identity.id
    if get_staff(staffID):
        rejected = get_staff_rejectedR(staffID)
        if rejected:
            return render_template('staffMain.html', accepted=acceptedRequests)
        return Response({"There are no rejected requests found for this user."}, status=404)
    return Response("Students cannot perform this action.", status=401)


# GET ALL COMPLETED REQUESTS
@request_views.route('/staffMain', methods=['GET'])
def view_all_completed_reqs():
    staffID = current_identity.id
    if get_staff(staffID):
        completed = get_staff_completedR(staffID)
        if completed:    
          return render_template('staffMain.html', completed=completedRequests)
        return Response({"There are no completed requests found for this user."}, status=404)
    return Response("Students cannot perform this action.", status=401)


# REQUESTS HISTORY
@request_views.route('/staffMain', methods=['GET'])
def reqs_history():
    staffID = current_identity.id
    if get_staff(staffID):
        completed = get_staff_completedR(staffID)
        rejected = get_staff_rejectedR(staffID)
        if completed:
            history = history + completed
        if rejected:
            history = history + rejected
    return render_template('staffMain.html', history=requestHistory)


## Create route for /<studentID>/<staffID>/writeRequest
# REQUEST A RECOMMENDATION
@request_views.route('/studentMain', methods=['POST'])
def create_request():
    studentID = current_identity.id
    if studentID:
        staff = get_staff(staffID)
        body = data.form
        request = create_request(studentID,staffID,body)
        if request:
            return request
        return Response({'The request could not be made.'}, status=422)
    return Response("Staff cannot perform this action.", status=401)


