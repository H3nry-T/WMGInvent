from flask import Flask, render_template, session, redirect, request, flash, url_for
from config import Config
from global_db_object import db
from services.UserService import AuthenticationService
from repositories.UserRepository import UserRepository
from forms.RegisterForm import RegisterForm
from forms.LoginForm import LoginForm
from werkzeug.security import generate_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from models.UserModel import User
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    return app, db

app, db = create_app()

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
@login_required
def home():
    return render_template('index.html', user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        try:
            user = AuthenticationService(UserRepository(db)).authenticate_user(username, password)
            login_user(user)
            return redirect('/')
        except Exception as e:
            flash('Invalid username or password', str(e))
            return redirect('/login')
    return render_template('login.html', form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        try:
            AuthenticationService(UserRepository(db)).register_user(username, password)
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('An error occurred during registration.', 'error')
            
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True, port=5000)