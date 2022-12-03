from App.models import Student
from App.database import db

# create_student()
#     student=
#     return student

def get_student(id):
    student = Student.query.get(id)
    if student:
        return student
    return None

def get_all_students():
    return Student.query.all()

def get_all_students_json():
    students = get_all_students()
    if not students:
        return None
    students = [student.toJSON() for student in students]
    return students

def get_all_recommendations_json():
    students = get_all_students()
    if not students:
        return None
    students = [student.toJSON_with_recommendations() for student in students]
    return students

def get_student_reclist(studentID):
    student = get_student(studentID)
    return student.recommendationList

def get_student_reclist_json(studentID):
    recs = get_student_reclist(studentID)
    if recs:
        return [rec.toJSON() for rec in recs]
    return None