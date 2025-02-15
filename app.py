from flask import Flask, render_template, session, redirect, request, flash
from config import Config
from global_db_object import db
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from models.UserModel import User
    
    return app, db

app, db = create_app()

@app.route('/')
def home():
    #grab the user from the session and check if user is logged in, if not logged in, take me to the login page.
    user = session.get('user')
    if not user:
        return redirect('/login')
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # TODO: Add your authentication logic here
        if username == "admin" and password == "password":
            session['user'] = username
            return redirect('/')
        else:
            flash('Invalid username or password')
            return redirect('/login')
            
    return render_template('login.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True, port=5000)