from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, InputRequired
from repositories.UserRepository import UserRepository
from services.UserService import AuthenticationService
from global_db_object import db

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(),
        Length(min=3, max=20, message="Username must be between 3 and 20 characters")
    ], render_kw={"placeholder": "Username"})
    
    password = PasswordField('Password', validators=[
        InputRequired(),
        Length(min=8, message="Password must be at least 8 characters long")
    ], render_kw={"placeholder": "Password"})
    
    confirm_password = PasswordField('Confirm Password', validators=[   
        InputRequired(),
        EqualTo('password', message='Passwords must match')
    ], render_kw={"placeholder": "Confirm Password"})
    
    submit = SubmitField('Register')

    def validate_username(self, username):
        username_is_allowed = AuthenticationService(UserRepository(db)).validate_username(username.data)
        if username_is_allowed:
            raise ValidationError('Username already exists. Please choose a different one.')
