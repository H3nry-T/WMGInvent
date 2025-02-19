from werkzeug.security import check_password_hash, generate_password_hash
from repositories.UserRepository import UserRepository
from models.UserModel import User
from typing import Dict

class AuthenticationService: 
    def __init__(self, user_repository: UserRepository): 
        self.user_repository = user_repository
    
    def register_user(self, username: str, password: str, role: str) -> User: 
        """Registers a new user and returns the user object if successful or raises an exception if not"""
        if self.username_available(username):
            hashed_password = generate_password_hash(password)
            user = self.user_repository.create_user(username, hashed_password, role)
            return user
        else: 
            raise Exception("problem with registering user")

    def username_available(self, username: str) -> bool:
        """Helps check if the username already exists before registering"""
        username_exists =  self.user_repository.get_user_by_username(username)
        if username_exists:
            # do not allow username to be used
            return False
        return True
    
    def authenticate_user(self, username: str, password: str) -> User: 
        """Authenticates the user and returns the user object if successful or raises an exception if not"""
        user = self.user_repository.get_user_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            return user
        else: 
            raise Exception("problem with authenticating user")