from flask import Flask, render_template, session, redirect, request, flash, url_for
from config import Config
from global_db_object import db
from services.UserService import AuthenticationService
from repositories.UserRepository import UserRepository
from forms.RegisterForm import RegisterForm
from forms.LoginForm import LoginForm
from werkzeug.security import generate_password_hash

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    return app, db

app, db = create_app()

@app.route('/')
def home():
    user = session.get('user')
    if user:
        return render_template('index.html', user=user)
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # TODO: Add your authentication logic here
        is_authenticated = False
        if username and password: 
            is_authenticated = AuthenticationService(UserRepository(db)).authenticate(username=username, password=password)
        
        if is_authenticated:
            session['user'] = username
            return redirect('/')
        else:
            flash('Invalid username or password')
            return redirect('/login')
            
    return render_template('login.html', form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        
        # Create new user
        user = {
            'username': form.username.data,
            'email': form.email.data,
            'password': hashed_password
        }
        
        try:
            UserRepository(db).create_user(user)
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('An error occurred during registration.', 'error')
            
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True, port=5000)