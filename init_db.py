# seed.py
from app import create_app, db
from models.UserModel import User

app, db = create_app()

with app.app_context():
    db.drop_all()   # optional: if you want to drop existing
    db.create_all()
    print("Database tables created successfully!")

    # Seed the data
    admin = User(username="admin", password_hash="...")
    user2 = User(username="john_doe", password_hash="...")

    db.session.add(admin)
    db.session.add(user2)
    db.session.commit()
    print("Database seeded with initial data!")
