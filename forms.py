from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    # retype_password = PasswordField('Retype Password', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired()])
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class FeedbackForm(FlaskForm):
    title = StringField('Username', validators=[InputRequired()])
    content = TextAreaField('Content', render_kw={'class': 'form-control', 'rows': 5}, validators=[InputRequired()])
