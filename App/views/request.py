from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    get_all_student_requests,
    get_all_student_requests_JSON,
    get_request,
    get_request_JSON,
    get_pendingR_byStud,
    get_acceptedR_byStud,
    get_acceptedR_byStaff,
    get_rejectedR_byStaff,
    get_completedR_byStaff
)

request_views = Blueprint('request_views', __name__, template_folder='../templates')

#GET ALL PENDING REQUESTS BY STUDENT ID



#GET ALL ACCEPTED REQUESTS BY STUDENT ID



#GET ALL ACCEPTED REQUESTS BY STAFF ID



#BUILD HISTORY: GET ALL REJECTED AND COMPLETED REQUESTS BY STAFF ID


