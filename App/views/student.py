from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response
from flask_jwt import jwt_required, current_identity
from flask_login import login_required, current_user

from App.controllers import (
    get_student,
    get_all_students,
    get_all_students_json,
    get_all_staff,
    get_staff,
    get_all_staff_json,
    get_student_reclist,
    get_student_pendingR,
    get_student_acceptedR,
    get_all_recommendations
)

student_views = Blueprint('student_views', __name__, template_folder='../templates')

## Render first version of studentMain.html
#VIEW ALL STAFF 
@student_views.route('/studentMain', methods=['GET'])
@login_required
def studentMain():
    studentID = current_user.id
    student = get_student(studentID)

    staff = get_all_staff()
    recommendations = get_student_reclist(studentID)

    acceptedrs = get_student_acceptedR(studentID)
    pendingrs = get_student_pendingR(studentID)
    
    selectedstaff=0
    return render_template('studentMain.html', student=student, staff=staff, recommendations=recommendations, acceptedrs=acceptedrs, pendingrs=pendingrs, selectedstaff=selectedstaff)


#VIEW ALL STAFF
# @student_views.route('/studentMain', methods=['GET'])
# @login_required 
# def view_all_staff():
#     staff = get_all_staff()
#     return render_template('studentMain.html', staff=staff)
#     # return Response({'Staff not found.'}, status=404)


 

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