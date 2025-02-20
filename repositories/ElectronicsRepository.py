from repositories.IRepository import IRepository
from models.ElectronicModel import Electronic
from typing import List
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
        return Electronic.query.filter_by(**filters).all()

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

    def search(self, filters) -> List[Electronic]:
        """
        Filter by LIKE name, description, or specification matching `keyword`.
        filter by price range if provided
        todo: filter by stock status
        """
        query = Electronic.query
        # destructure filters
        keyword = filters["keyword"]
        min_price = filters["min_price"]
        max_price = filters["max_price"]

        # construct search query like keyword
        if keyword:
            query = query.filter(
                (Electronic.name.ilike(f"%{keyword}%")) |
                (Electronic.description.ilike(f"%{keyword}%")) |
                (Electronic.specification.ilike(f"%{keyword}%"))
            )
        
        # filter by price range
        if min_price is not None:
            query = query.filter(Electronic.price >= min_price)
        if max_price is not None:
            query = query.filter(Electronic.price <= max_price)
        
        return query.all()

    
    
    
    