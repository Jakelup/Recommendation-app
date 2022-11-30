from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    # send_recommendation, REMOVED DURING REFACTORING OF RECOMMENDATION.PY
    get_all_recommendations_json,
    get_student,
    get_recommendation,
    get_student_reclist_json
)

recommendation_views = Blueprint('recommendation_views', __name__, template_folder='../templates')


## Create route for /<staffID>/<reqID>/writeRecommendation
#(Use change_status(reqID, "Completed"))








## ARCHIVE - Original Code:

# SEND RECOMMENDATION TO STUDENT
@recommendation_views.route('/send', methods=['POST'])
@jwt_required()
def sendRecommendation():
    if not get_student(current_identity.id):
        data = request.get_json()
        student = get_student(data['sentToStudentID'])
        if not student:
            return Response({'student not found'}, status=404)
        # send_recommendation(current_identity.id, data['sentToStudentID'], data['recURL'])
        return Response({'recommendation sent'}, status=200)
    return Response({"students cannot perform this action"}, status=401)


# VIEW RECOMMENDATION
@recommendation_views.route('/recommendations/<recID>', methods=['GET'])
@jwt_required()
def view_recommendation(recID):
    studID = current_identity.id
    student = get_student(studID)
    if student:
        recs = get_student_reclist_json(studID)
        if not recs:
            return Response({"no recommendations found for this user"}, status=404)
        rec = get_recommendation(studID, recID)
        if rec:
            return jsonify(rec)
        return Response({'recommendation with id ' + recID + ' not found'}, status=404)
    return Response({"staff cannot perform this action"}, status=401)


# routes for testing purposes
# View all recommendations for all users
@recommendation_views.route('/recs', methods=['GET'])
def get_all_recs():
    return jsonify(get_all_recommendations_json())
    
