from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, InputRequired
from repositories.UserRepository import UserRepository
from services.AuthService import AuthenticationService
from global_db_object import db

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(),
        Length(min=3, max=20, message="Username must be between 3 and 20 characters")
    ], render_kw={"placeholder": "Username"})
    
    password = PasswordField('Password', validators=[
        InputRequired(),
        Length(min=8, message="Password must be at least 8 characters long")
    ], render_kw={"placeholder": "Password"})
    
    submit = SubmitField('Login')

