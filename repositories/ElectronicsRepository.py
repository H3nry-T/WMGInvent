from repositories.IRepository import IRepository
from models.ElectronicModel import Electronic
from typing import List, Optional
class ElectronicsRepository(IRepository):
    def __init__(self, db):
        self.db = db
        
    def get_by_id(self, id: int) -> Optional[Electronic]:
        return Electronic.query.get(id)
    
    def get_all(self): 
        return Electronic.query.all()
    
    def create(self, electronic: Electronic) -> Electronic:
        try:
            self.db.session.add(electronic)
            self.db.session.commit()
            return electronic
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def update_by_id(self, id, entity): 
        self.db.session.query(Electronic).filter_by(id=id).update(entity)
        self.db.session.commit()
        return entity

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
    
    def count(self):
        """Count total entities, optionally filtered"""
        return Electronic.query.count()

    def search(self, filters) -> List[Electronic]:
        """
        Filter and sort electronics.
        
        filters : {
            keyword: str, 
            min_price: float, 
            max_price: float,
            stock_status: str,
            sort_by: str,  # 'price_asc', 'price_desc', 'stock_asc', 'stock_desc'
        }
        """
        query = Electronic.query
        keyword = filters["keyword"]
        min_price = filters["min_price"]
        max_price = filters["max_price"]
        stock_status = filters["stock_status"]
        sort_by = filters.get("sort_by")

        if keyword:
            query = query.filter(
                (Electronic.name.ilike(f"%{keyword}%")) |
                (Electronic.description.ilike(f"%{keyword}%")) |
                (Electronic.specification.ilike(f"%{keyword}%"))
            )
        
        if min_price is not None:
            query = query.filter(Electronic.price >= min_price)
        if max_price is not None:
            query = query.filter(Electronic.price <= max_price)
        
        if stock_status:
            if stock_status == "in_stock":
                query = query.filter(Electronic.stock > 0)
            elif stock_status == "low_stock":
                query = query.filter(Electronic.stock <= 5, Electronic.stock > 0)
            elif stock_status == "out_of_stock":
                query = query.filter(Electronic.stock == 0)

        if sort_by:
            if sort_by == "price_asc":
                query = query.order_by(Electronic.price.asc())
            elif sort_by == "price_desc":
                query = query.order_by(Electronic.price.desc())
            elif sort_by == "stock_asc":
                query = query.order_by(Electronic.stock.asc())
            elif sort_by == "stock_desc":
                query = query.order_by(Electronic.stock.desc())
        
        return query.all()

    def update(self, electronic: Electronic) -> Electronic:
        self.db.session.commit()
        return electronic
    
    def delete(self, electronic: Electronic) -> bool:
        try:
            self.db.session.delete(electronic)
            self.db.session.commit()
            return True
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    
    
    
    