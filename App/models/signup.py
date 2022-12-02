from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email

class StudentRegister(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    name = StringField('Name', validators=[InputRequired()])
    faculty = StringField('Faculty', validators=[InputRequired()])
    department = StringField('Department', validators=[InputRequired()])

    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})


class StaffRegister(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')
    name = StringField('Name', validators=[InputRequired()])
    faculty = StringField('Faculty', validators=[InputRequired()])
    department = StringField('Department', validators=[InputRequired()])

    submit = SubmitField('Sign Up', render_kw={'class': 'btn waves-effect waves-light white-text'})
