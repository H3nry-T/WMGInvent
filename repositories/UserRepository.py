from models.UserModel import User

class UserRepository: 
    def __init__(self, db): 
        self.db = db 
    
    def get_user_by_username(self, username): 
        return User.query.filter_by(username=username).first()

    def find_by_username(self, username):
        # Implement database query
        return self.db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

    def find_by_email(self, email):
        # Implement database query
        return self.db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()

    def create_user(self, user):
        # Implement user creation
        self.db.execute(
            'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
            (user['username'], user['email'], user['password'])
        )
        self.db.commit()