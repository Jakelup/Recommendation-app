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
    get_staff_pendingR
)

request_views = Blueprint('request_views', __name__, template_folder='../templates')


## Create Route called /studentMain to: 
    #GET ALL PENDING REQUESTS BY STUDENT ID 
    #GET ALL ACCEPTED REQUESTS BY STUDENT ID



## Create Route called /staffMain to: 
    #GET ALL ACCEPTED REQUESTS BY STAFF ID
    #BUILD HISTORY: GET ALL REJECTED AND COMPLETED REQUESTS BY STAFF ID



## Create route for /<studentID>/<staffID>/writeRequest



## Create route for /<staffID>/<reqID>/writeRecommendation
#(Use change_status(reqID, "Completed"))
