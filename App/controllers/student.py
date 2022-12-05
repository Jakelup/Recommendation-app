from App.models import Student, Recommendation
from App.database import db



# STUDENT SIGNUP
def create_student(id, username, password, name, faculty, department):
    newStudent = Student(id=id, username=username, password=password, name=name, faculty=faculty, department=department)
    try:
        db.session.add(newStudent)
        db.session.commit()
        return newStudent
    except IntegrityError: # attempted to insert a duplicate user or other errors
        db.session.rollback()
        return None
    #     return Response({'user already exists with this username'}, status=400) #error message
    # return Response({'user created successfully'}, status=201) # success


# def create_student(id, username, password, name, faculty, department):
#     newstudent = Student(id=id, username=username, password=password, name=name, faculty=faculty, department=department)
#     return newstudent

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