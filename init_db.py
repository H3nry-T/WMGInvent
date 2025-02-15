import os
from extensions import db
from models.UserModel import User
from werkzeug.security import generate_password_hash
from flask import Flask
from config import Config

def seed_database():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, 'database.db')
    
    print(f"Current working directory: {os.getcwd()}")
    print(f"Database path: {db_path}")

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        
        if not os.path.exists(db_path):
            print("ERROR: Database file was not created!")
            return

        admin = User()
        admin.username = "admin"
        admin.password_hash = generate_password_hash("admin123")
        db.session.add(admin)
        db.session.commit()
        
        print(f"Database created successfully at {db_path}")
        print(f"Size: {os.path.getsize(db_path)} bytes")
        print(f"Users: {[user.username for user in User.query.all()]}")

if __name__ == "__main__":
    seed_database()
