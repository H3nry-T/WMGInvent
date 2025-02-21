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
    
    def update_electronics_by_id(self, id, electronic): 
        return self.electronics_repository.update_by_id(id, electronic)
    
    def create_electronic(self, electronic): 
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
        return self.electronics_repository.update(electronic)
    
    def delete_electronic(self, electronic: Electronic) -> bool:
        return self.electronics_repository.delete(electronic)
    
    
    
    
    
    
    