from repositories.IRepository import IRepository
from models.ElectronicModel import Electronic
from repositories.ElectronicsRepository import ElectronicsRepository
from typing import List, Optional

class ElectronicsService: 
    def __init__(self, electronics_repository: ElectronicsRepository):
        self.electronics_repository = electronics_repository

    def get_all_electronics(self) -> List[Electronic]:
        return self.electronics_repository.get_all()
    
    def get_electronics_by_id(self, id) -> Optional[Electronic]:
        return self.electronics_repository.get_by_id(id)
    
    def update_electronics_by_id(self, id: int, updates: dict) -> Optional[Electronic]:
        electronic = self.get_electronics_by_id(id)
        if not electronic:
            return None
        
        # go through dictionary and update the electronic object
        for key, value in updates.items():
            if hasattr(electronic, key):
                setattr(electronic, key, value)
            
        return self.electronics_repository.update(electronic)
    
    def create_electronic(self, electronic: Electronic) -> Electronic:
        return self.electronics_repository.create(electronic)
    
    def count_electronics(self): 
        return self.electronics_repository.count()
    
    def search_electronics(
        self, 
        keyword: str, 
        min_price: Optional[float] = None, 
        max_price: Optional[float] = None, 
        stock_status: Optional[str] = None,
        sort_by: Optional[str] = None
    ): 
        filters = {
            "keyword": keyword, 
            "min_price": min_price, 
            "max_price": max_price,
            "stock_status": stock_status,
            "sort_by": sort_by
        }
        if not any(filters.values()):
            return self.electronics_repository.get_all()
        return self.electronics_repository.search(filters)
    
    def update_electronic(self, electronic: Electronic) -> Electronic:
        """updates electronic object by providing the electronic object NOT the ID"""
        return self.electronics_repository.update(electronic)
    
    def delete_electronic(self, electronic: Electronic) -> bool:
        return self.electronics_repository.delete(electronic)
    
    
    
    
    
    
    