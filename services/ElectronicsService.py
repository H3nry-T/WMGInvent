from repositories.IRepository import IRepository
from models.ElectronicModel import Electronic
from typing import List, Optional

class ElectronicsService: 
    def __init__(self, inventory_repository: IRepository):
        self.inventory_repository = inventory_repository

    def get_all_electronics(self) -> List[Electronic]:
        return self.inventory_repository.get_all()
    
    def get_electronics_by_id(self, id):
        return self.inventory_repository.get_by_id(id)
    
    def create_electronic(self, electronic): 
        return self.inventory_repository.create(electronic)
    
    def count_electronics(self): 
        return self.inventory_repository.count()
    
    def get_paginated_electronics(self, page, per_page): 
        return self.inventory_repository.get_paginated(page, per_page)
    
    def search_electronics(self, keyword: str, min_price: Optional[float] = None, max_price: Optional[float] = None): 
        filters = {
            "keyword": keyword, 
            "min_price": min_price, 
            "max_price": max_price
        }
        if not keyword and min_price is None and max_price is None:
            return self.inventory_repository.get_all()
        return self.inventory_repository.search(filters)
    
    
    
    
    
    
    