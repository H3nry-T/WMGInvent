# seed.py
from app import create_app
from global_db_object import db
from werkzeug.security import generate_password_hash
from models.UserModel import User
app, _ = create_app()  # Destructure the tuple to get just the app

with app.app_context():
    db.drop_all()  
    db.create_all()
    print("Created tables in: ", db.engine.url, db.engine.dialect.name)
    print("Tables: ", db.metadata.tables.keys())

    # Seed the data
    admin = User()
    admin.username = "admin"
    admin.password_hash = generate_password_hash("admin123")
    db.session.add(admin)
    db.session.commit()
    print("Database seeded with initial data!")
