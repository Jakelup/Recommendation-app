from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response
from flask_jwt import jwt_required, current_identity
from flask_login import login_required, current_user

from App.controllers import (
    get_student,
    get_all_students,
    get_all_students_json,
    get_all_staff,
    get_all_staff_json,
    get_student_reclist_json,
    get_student_pendingR,
    get_student_acceptedR,
)

student_views = Blueprint('student_views', __name__, template_folder='../templates')

## Render first version of studentMain.html
@student_views.route('/studentMain', methods=['GET'])
# @login_required -- enable this once login is set up
def load_page():
    return render_template('studentMain.html')



    ###REQUEST ROUTES###

# GET ALL PENDING REQUESTS
@student_views.route('/studentMain', methods=['GET'])
def view_all_pending_reqs():
    studentID = current_identity.id
    if get_student(studentID):
        pending = get_student_pendingR(studentID)
        if pending:
            return pending
        return Response({'There are no pending request found for this user.'}, status=404)
    return Response("Staff cannot perform this action.", status=401)

# GET ALL ACCEPTED REQUESTS
@student_views.route('/studentMain', methods=['GET'])
    studentID = current_identity.id
    if get_student(studentID):
        accepted = get_student_acceptedR(studentID)
        if accepted:
            return accepted
        return Response({'There are no accepted request found for this user.'}, status=404)
    return Response("Staff cannot perform this action.", status=401)

# REQUEST A RECOMMENDATION
@student_views.route('/studentMain', methods=['POST'])
def create_request():
    staff = get_all_staff_json()
    if staff:
        return staff
    return Response({'Staff not found.'}, status=404)



    ###STAFF###

# JSON VIEW ALL STAFF
@student_views.route('/studentMain', methods=['GET'])
def view_all_staff():
    staff = get_all_staff_json()
    if staff:
        return staff
    return Response({'Staff not found.'}, status=404)



    ###RECCOMMENDATIONS###

# VIEW RECOMMENDATION LISTING
@student_views.route('/studentMain', methods=['GET'])
@jwt_required()
def get_recommendations():
    studentID = current_identity.id
    if get_student(studentID):
        recs = get_student_reclist_json(studentID)
        if recs:
            return jsonify(recs)
        return Response({'There are no recommendations found for this user.'}, status=404)
    return Response("staff cannot perform this action.", status=401)

'''


# SEARCH STAFF
@student_views.route('/search', methods=['GET'])
@jwt_required()
def searchStaff():
    id = current_identity.id
    if get_student(id):
        sID = request.args.get('staffID')
        fn = request.args.get('firstName')
        ln = request.args.get('lastName')
        if (sID):
            staff=search_staff("ID", sID)
        else:
            if (fn and ln):
                staff=search_staff("name", fn + "," + ln)
            else:
                if (fn):
                    staff=search_staff("firstName", fn)
                else:
                    if(ln):
                        staff=search_staff("lastName", ln)
        if staff:
            return staff
        return Response({'staff member not found'}, status=404)
    return Response({"staff cannot perform this action"}, status=401)

# Routes for testing purposes
@student_views.route('/view/students', methods=['GET'])
def get_students_page():
    students = get_all_students()
    return render_template('users.html', users=students)

# JSON view all Students
@student_views.route('/students', methods=['GET'])
def get_students():
    students = get_all_students_json()
    return jsonify(students)
'''