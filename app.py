from flask import Flask, render_template, session, redirect, request, flash, url_for
from config import Config
from global_db_object import db
from services.AuthService import AuthenticationService
from repositories.UserRepository import UserRepository
from forms.RegisterForm import RegisterForm
from forms.LoginForm import LoginForm
from werkzeug.security import generate_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from models.UserModel import User
from flask_login import LoginManager
from routes.auth_routes import auth_routes
from flask_migrate import Migrate
from routes.electronics_routes import electronics_routes
def create_app(config_class=Config):
    app = Flask(__name__,
                static_folder='static',
                static_url_path='/static')
    app.config.from_object(config_class)
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' # type: ignore
    login_manager.login_message = 'Please log in to access this page.'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    app.register_blueprint(auth_routes)
    app.register_blueprint(electronics_routes)
    return app

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=5000)