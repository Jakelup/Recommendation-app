from flask import Blueprint, render_template, jsonify, flash, request, send_from_directory, Response, redirect, url_for
from flask_jwt import jwt_required, current_identity
from flask_login import login_required, current_user
from App.models import Status

from App.controllers import (
    # send_recommendation, REMOVED DURING REFACTORING OF RECOMMENDATION.PY
    get_all_recommendations_json,
    get_student,
    get_recommendation,
    get_student_reclist_json, 
    get_student_reclist,
    get_request,
    get_staff,
    get_staff_acceptedR,
    get_staff_historyR,
    get_all_notifs_unseen,
    create_recommendation,
    change_status
)

recommendation_views = Blueprint('recommendation_views', __name__, template_folder='../templates')


#SELECT REQUEST TO BEGIN WRITING RECOMMENDATION
@recommendation_views.route('/staffMain/selectReq', methods=['GET', 'POST'])
@login_required 
def start_recommendation():
    # data = request.form

    ##get request according to id selected
    selectedRec = get_request(request.form.get('reqID'))
    
    staffID = current_user.id
    staff = get_staff(staffID)

    ##get accepted requests
    acceptedrs = get_staff_acceptedR(staffID)
        
    ##get pending and completed requests
    historyrs = get_staff_historyR(staffID)

    ##get all notifications
    notifications = get_all_notifs_unseen(staff)
    
    return render_template('staffMain.html', staff=staff, historyrs=historyrs, acceptedrs=acceptedrs, selectedRec=selectedRec, notifications=notifications)


   
## Create route for /<staffID>/<reqID>/writeRecommendation
#(Use change_status(reqID, "Completed"))
# CREATE A RECOMMENDATION
@recommendation_views.route('/staffMain/writeRecommendation', methods=['GET', 'POST'])
@login_required 
def write_recommendation():
    data = request.form

    staff = get_staff(current_user.id)
    id = data['id']
    selectedReq = get_request(id)

    if selectedReq == None:
        render_template('index.html')

    selectedReq = change_status(selectedReq.requestID, Status.COMPLETED)

    recommendation = create_recommendation(current_user.id, selectedReq.studentId, data['body'])
    
    flash('Recommendation created and sent!')
    return redirect(url_for('staff_views.staffMain'))



# ## ARCHIVE - Original Code & code moved after refinement:

#    ###RECOMMENDATIONS###

# # VIEW RECOMMENDATION LISTING
# @recommendation_views.route('/studentMain', methods=['GET'])
# @login_required 
# @jwt_required()
# def get_recommendations():
#     studentID = current_identity.id
#     if get_student(studentID):
#         recs = get_student_reclist(studentID)
#     return render_template('studentMain.html', staff=staff, recommendation=recs)
    
#     #     if recs:
#     #         return jsonify(recs)
#     #     return Response({'There are no recommendations found for this user.'}, status=404)
#     # return Response("staff cannot perform this action.", status=401)



# # SEND RECOMMENDATION TO STUDENT
# @recommendation_views.route('/send', methods=['POST'])
# @jwt_required()
# def sendRecommendation():
#     if not get_student(current_identity.id):
#         data = request.get_json()
#         student = get_student(data['sentToStudentID'])
#         if not student:
#             return Response({'student not found'}, status=404)
#         # send_recommendation(current_identity.id, data['sentToStudentID'], data['recURL'])
#         return Response({'recommendation sent'}, status=200)
#     return Response({"students cannot perform this action"}, status=401)


# # VIEW RECOMMENDATION
# @recommendation_views.route('/recommendations/<recID>', methods=['GET'])
# @jwt_required()
# def view_recommendation(recID):
#     studID = current_identity.id
#     student = get_student(studID)
#     if student:
#         recs = get_student_reclist_json(studID)
#         if not recs:
#             return Response({"no recommendations found for this user"}, status=404)
#         rec = get_recommendation(studID, recID)
#         if rec:
#             return jsonify(rec)
#         return Response({'recommendation with id ' + recID + ' not found'}, status=404)
#     return Response({"staff cannot perform this action"}, status=401)


# # routes for testing purposes
# # View all recommendations for all users
# @recommendation_views.route('/recs', methods=['GET'])
# def get_all_recs():
#     return jsonify(get_all_recommendations_json())
    
