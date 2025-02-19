from werkzeug.security import check_password_hash, generate_password_hash
from repositories.UserRepository import UserRepository
from models.UserModel import User
from typing import Dict

class AuthenticationService: 
    def __init__(self, user_repository: UserRepository): 
        self.user_repository = user_repository
    
    # Registers a new user and returns the user object if successful or raises an exception if not
    def register_user(self, username: str, password: str) -> User: 
        if self.username_available(username):
            hashed_password = generate_password_hash(password)
            user = self.user_repository.create_user(username, hashed_password)
            return user
        else: 
            raise Exception("problem with registering user")

    # Helps check if the username already exists before registering
    def username_available(self, username: str) -> bool:
        username_exists =  self.user_repository.get_user_by_username(username)
        if username_exists:
            # do not allow username to be used
            return False
        return True
    
    # Authenticates the user and returns the user object if successful or raises an exception if not
    def authenticate_user(self, username: str, password: str) -> User: 
        user = self.user_repository.get_user_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            return user
        else: 
            raise Exception("problem with authenticating user")