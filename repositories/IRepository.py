from abc import ABC, abstractmethod

class IRepository(ABC): 
    @abstractmethod
    def get_by_id(self, id: int): 
        pass
    
    @abstractmethod
    def get_all(self): 
        pass
    
    @abstractmethod
    def create(self, entity): 
        pass
    
    @abstractmethod
    def update_by_id(self, id: int, entity): 
        pass

    @abstractmethod
    def delete_by_id(self, id: int): 
        pass
    
    