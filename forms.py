from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username'), validators=[DataRequired(), Length(min=4, max=20)]
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=15)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(),    
                                                                     EqualTo('password',
                                                                             message='Passwords must match.')])
    submit = SubmitField('Register')

class CreateEventForm(FlaskForm):
    location_name = SelectField('Location')
    type_of = SelectField('type')
    difficulty = StringField('difficulity')
    distance = StringField('distance')
    comment = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Add Event')



class EditEventForm(FlaskForm):
    location_name = SelectField('Location')
    type_of = SelectField('type')
    difficulty = StringField('difficulity')
    distance = StringField('distance')
    comment = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Update Event')


class ConfirmDelete(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Delete this Event')