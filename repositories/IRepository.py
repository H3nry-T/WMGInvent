from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class IRepository(ABC): 
    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Any]: 
        pass
    
    @abstractmethod
    def get_all(self) -> List[Any]: 
        pass
    
    @abstractmethod
    def create(self, entity: Any) -> Any: 
        pass
    
    @abstractmethod
    def update_by_id(self, id: int, entity: Any) -> Optional[Any]: 
        pass

    @abstractmethod
    def delete_by_id(self, id: int) -> bool: 
        pass
    
    @abstractmethod
    def get_by_filter(self, column: str, value: str) -> List[Any]: 
        """Specify a column and a value to filter the results"""
        pass

    @abstractmethod
    def get_by_filters(self, filters: Dict[str, Any]) -> List[Any]:
        """Get entities matching multiple filter criteria"""
        pass

    @abstractmethod
    def bulk_create(self, entities: List[Any]) -> List[Any]:
        """Create multiple entities at once"""
        pass

    @abstractmethod
    def bulk_update(self, entities: List[Dict[str, Any]]) -> List[Any]:
        """Update multiple entities at once"""
        pass
    
    @abstractmethod
    def get_paginated(self, page: int, per_page: int) -> Dict[str, Any]:
        """Get paginated results with metadata"""
        pass
    
    @abstractmethod
    def count(self, filters: Optional[Dict[str, Any]] = None) -> int:
        """Count total entities, optionally filtered"""
        pass
