from repositories.IRepository import IRepository
from models.ElectronicModel import Electronic

class ElectronicsRepository(IRepository):
    def __init__(self, db):
        self.db = db
        
    def get_by_id(self, id): 
        return Electronic.query.get(id)
    
    def get_all(self): 
        return Electronic.query.all()
    
    def create(self, entity): 
        self.db.session.add(entity)
        self.db.session.commit()
        return entity
    
    def update_by_id(self, id, entity): 
        pass

    def delete_by_id(self, id): 
        pass
    
    def get_by_filter(self, column, value): 
        """Specify a column and a value to filter the results"""
        pass

    def get_by_filters(self, filters):
        """Get entities matching multiple filter criteria"""
        pass

    def bulk_create(self, entities):
        """Create multiple entities at once"""
        pass

    def bulk_update(self, entities):
        """Update multiple entities at once"""
        pass
    
    def get_paginated(self, page, per_page):
        """Get paginated results with metadata"""
        return Electronic.query.paginate(page=page, per_page=per_page)
    
    def count(self, filters):
        """Count total entities, optionally filtered"""
        return Electronic.query.count()
    
    
    
    