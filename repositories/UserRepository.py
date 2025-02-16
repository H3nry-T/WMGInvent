from models.UserModel import User

class UserRepository: 
    def __init__(self, db): 
        self.db = db 
    
    def get_user_by_username(self, username): 
        return User.query.filter_by(username=username).first()