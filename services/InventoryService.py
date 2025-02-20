class InventoryService:
    def __init__(self, product_repository):
        self.product_repository = product_repository
    
    def get_all_products(self):
        return self.product_repository.get_all()
    
    def get_product_by_id(self, id):
        return self.product_repository.get_by_id(id) 