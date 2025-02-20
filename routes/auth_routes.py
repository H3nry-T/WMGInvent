# routes/auth_routes.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from forms.LoginForm import LoginForm
from forms.RegisterForm import RegisterForm
from services.AuthService import AuthenticationService
from repositories.UserRepository import UserRepository
from global_db_object import db
from services.ElectronicsService import ElectronicsService
from repositories.ElectronicsRepository import ElectronicsRepository

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/')
@login_required
def home():
    electronics_service = ElectronicsService(ElectronicsRepository(db))
    electronics = electronics_service.get_all_electronics()

    return render_template('index.html', user=current_user, electronics=electronics)

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        try:
            user = AuthenticationService(UserRepository(db)).authenticate_user(username, password)
            login_user(user)
            return redirect(url_for('auth.home'))
        except Exception as e:
            flash('Invalid username or password', str(e))
            return redirect(url_for('auth.login'))
    return render_template('login.html', form=form)

@auth_routes.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        role = form.role.data
        try:
            AuthenticationService(UserRepository(db)).register_user(username, password, role)
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash('An error occurred during registration.', 'error')
            
    return render_template('register.html', form=form)

@auth_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))