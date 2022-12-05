from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response, redirect, url_for
from flask_jwt import jwt_required, current_identity
from flask_login import login_required, current_user

from App.controllers import (
    get_all_student_requests,
    get_all_student_requests_JSON,
    get_request,
    get_student,
    get_all_staff,
    get_staff,
    get_request_JSON,
    change_status,
    get_student_pendingR,
    get_student_acceptedR,
    get_staff_acceptedR,
    get_staff_pendingR,
    get_student_reclist,
    create_request,
    create_notification
)

request_views = Blueprint('request_views', __name__, template_folder='../templates')

#SELECT STAFF TO BEGIN WRITING REQUEST
@request_views.route('/studentMain/selectStaff', methods=['GET', 'POST'])
@login_required 
def start_request():
    data = request.form
    selectedstaff = get_staff(data['staffId'])

    studentID = current_user.id
    student = get_student(studentID)
    staff = get_all_staff()
    recommendations = get_student_reclist(studentID)
    acceptedrs = get_student_acceptedR(studentID)
    pendingrs = get_student_pendingR(studentID)

    return render_template('studentMain.html', student=student, staff=staff, recommendations=recommendations, acceptedrs=acceptedrs, pendingrs=pendingrs, selectedstaff=selectedstaff)

## Create route for /writeRequest
# REQUEST A RECOMMENDATION
@request_views.route('/studentMain/writeRequest', methods=['GET', 'POST'])
@login_required 
def write_request():
    data = request.form
    studentID = current_user.id
    student = get_student(studentID)

    if studentID:
        therequest = create_request(studentID, data['staffId'], data['body'])

    ##CREATE NOTIFICATION FOR THAT REQUEST
    notification = create_notification(therequest, student.name)

    return redirect(url_for('student_views.studentMain'))


    #     return Response({'The request could not be made.'}, status=422)
    # return Response("Staff cannot perform this action.", status=401)


## Create Route called /staffMain to: 
    #GET ALL ACCEPTED REQUESTS BY STAFF ID
    #BUILD HISTORY: GET ALL REJECTED AND COMPLETED REQUESTS BY STAFF ID
    
# GET ALL PENDING REQUESTS (realized not needed)
# @request_views.route('/staffMain', methods=['GET'])
# @login_required 
# def view_all_pending_reqs():
#     staffID = current_identity.id
#     if get_staff(staffID):
#         pending = get_staff_pendingR(staffID)
#         if pending:
#             return render_template('staffMain.html', pending=pendingRequests)
#         return Response({'There are no pending requests found for this user.'}, status=404)
#     return Response("Student cannot perform this action.", status=401)



# # REQUESTS HISTORY (realized not needed)
# @request_views.route('/staffMain', methods=['GET'])
# @login_required 
# def reqs_history():
#     staffID = current_identity.id
#     if get_staff(staffID):
#         completed = get_staff_completedR(staffID)
#         rejected = get_staff_rejectedR(staffID)
        
#     return render_template('staffMain.html', completed=completed, rejected=rejected)


##ARCHIVE BECAUSE FIRST INSTANCE OF STUDENTMAIN ROUTE HANDLES THESE FUNCTIONS:
# ## Create Route called /studentMain to:
# # GET ALL PENDING REQUESTS
# @request_views.route('/studentMain', methods=['GET'])
# @login_required 
# def view_all_pending_reqs():
#     studentID = current_identity.id
#     if get_student(studentID):
#         pending = get_student_pendingR(studentID)
#         if pending:
#             return render_template('staffMain.html', pending=pendingRequests)
#         return Response({'There are no pending requests found for this user.'}, status=404)
#     return Response("Staff cannot perform this action.", status=401)

# # GET ALL ACCEPTED REQUESTS
# @request_views.route('/studentMain', methods=['GET'])
# @login_required 
# def view_all_accepted_reqs():
#     studentID = current_identity.id
#     if get_student(studentID):
#         accepted = get_student_acceptedR(studentID)
#         if accepted:
#             return render_template('studentMain.html', accepted=acceptedRequests)
#         return Response({'There are no accepted requests found for this user.'}, status=404)
#     return Response("Staff cannot perform this action.", status=401)



##ARCHIVE BECAUSE FIRST INSTANCE OF STAFF ROUTE HANDLES THESE FUNCTIONS:
# # GET ALL ACCEPTED REQUESTS
# @request_views.route('/staffMain', methods=['GET'])
# @login_required 
# def view_all_accepted_reqs():
#     staffID = current_identity.id
#     if get_staff(staffID):
#         accepted = get_staff_acceptedR(staffID)
#         if accepted:
#             return render_template('staffMain.html', accepted=acceptedRequests)
#         return Response({'There are no accepted requests found for this user.'}, status=404)
#     return Response("Students cannot perform this action.", status=401)

# # GET ALL REJECTED REQUESTS
# @request_views.route('/staffMain', methods=['GET'])
# @login_required 
# def view_all_rejected_reqs():
#     staffID = current_identity.id
#     if get_staff(staffID):
#         rejected = get_staff_rejectedR(staffID)
#         if rejected:
#             return render_template('staffMain.html', accepted=acceptedRequests)
#         return Response({"There are no rejected requests found for this user."}, status=404)
#     return Response("Students cannot perform this action.", status=401)


# # GET ALL COMPLETED REQUESTS
# @request_views.route('/staffMain', methods=['GET'])
# @login_required 
# def view_all_completed_reqs():
#     staffID = current_identity.id
#     if get_staff(staffID):
#         completed = get_staff_completedR(staffID)
#         if completed:    
#           return render_template('staffMain.html', completed=completedRequests)
#         return Response({"There are no completed requests found for this user."}, status=404)
#     return Response("Students cannot perform this action.", status=401)
