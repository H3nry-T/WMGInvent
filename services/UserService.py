from werkzeug.security import check_password_hash

class AuthenticationService: 
    def __init__(self, user_repository): 
        self.user_repository = user_repository
    
    def register_user(self, username, password): 
        if self.user_repository.get_user_by_username(username): 
            return False, "Username already exists"
        user = self.user_repository.create_user(username, password)
        return True, "User registered successfully"

    # Helps check if the username already exists before registering
    def validate_username(self, username):
        username_exists =  self.user_repository.get_user_by_username(username)
        if username_exists:
            # do not allow username to be used
            return False
        return True
    
    def authenticate(self, username: str, password: str) -> bool: 
        user = self.user_repository.get_user_by_username(username)
        if not user:
            return False
        return check_password_hash(user.password_hash, password)