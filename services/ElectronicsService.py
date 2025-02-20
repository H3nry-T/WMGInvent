from repositories.IRepository import IRepository
from models.ElectronicModel import Electronic
from typing import List, Optional

class ElectronicsService: 
    def __init__(self, electronics_repository: IRepository):
        self.electronics_repository = electronics_repository

    def get_all_electronics(self) -> List[Electronic]:
        return self.electronics_repository.get_all()
    
    def get_electronics_by_id(self, id):
        return self.electronics_repository.get_by_id(id)
    
    def create_electronic(self, electronic): 
        return self.electronics_repository.create(electronic)
    
    def count_electronics(self): 
        return self.electronics_repository.count()
    
    def get_paginated_electronics(self, page, per_page): 
        return self.electronics_repository.get_paginated(page, per_page)
    
    def search_electronics(self, keyword: str, min_price: Optional[float] = None, max_price: Optional[float] = None, stock_status: Optional[str] = None): 
        filters = {
            "keyword": keyword, 
            "min_price": min_price, 
            "max_price": max_price,
            "stock_status": stock_status
        }
        if not keyword and min_price is None and max_price is None and stock_status is None:
            return self.electronics_repository.get_all()
        return self.electronics_repository.search(filters)
    
    
    
    
    
    
    