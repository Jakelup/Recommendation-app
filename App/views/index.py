from flask import Blueprint, redirect, render_template, request, send_from_directory

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/chooseAccount/student', methods=['GET'])
def loadstudent():
    usertype = "student"
    return render_template('account.html', usertype=usertype)

@index_views.route('/chooseAccount/staff', methods=['GET'])
def loadstaff():
    usertype = "staff"
    return render_template('account.html', usertype=usertype)
