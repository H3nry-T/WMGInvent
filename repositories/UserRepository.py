from models.UserModel import User
from typing import Dict
from repositories.IRepository import IRepository

class UserRepository(IRepository): 
    def __init__(self, db): 
        self.db = db 

    def get_by_id(self, id): 
        pass
    
    def get_all(self): 
        pass
    
    def create(self, user): 
        pass
    
    def update_by_id(self, id, user): 
        pass
    
    def delete_by_id(self, id): 
        pass
        
    def get_by_filters(self, filters): 
        pass
    
    def bulk_create(self, users): 
        pass
    
    def bulk_update(self, users): 
        pass

    def get_paginated(self, page, per_page): 
        pass
    
    def count(self, filters): 
        pass

    def get_by_filter(self, column, value): 
        filter_dict = {column: value}
        return User.query.filter_by(**filter_dict).first()
    
    def get_user_by_username(self, username: str) -> User | None: 
        return self.get_by_filter("username", username)

    def create_user(self, username: str, hashed_password: str, role: str) -> User:
        user = User()
        user.username = username
        user.password_hash = hashed_password
        user.role = role
        self.db.session.add(user)
        self.db.session.commit()
        return user
    
    def search(self, keyword): 
        pass