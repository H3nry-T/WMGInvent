from models.UserModel import User
from typing import Dict
class UserRepository: 
    def __init__(self, db): 
        self.db = db 
    
    def get_user_by_username(self, username): 
        return User.query.filter_by(username=username).first()

    def find_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def create_user(self, username: str, hashed_password: str):
        user = User()
        user.username = username
        user.password_hash = hashed_password
        self.db.session.add(user)
        self.db.session.commit()
        return user