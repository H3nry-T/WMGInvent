
class ProductCategory:
    ELECTRONICS = "electronics"
    FURNITURE = "furniture"
    AUTO_PARTS = "auto_parts"
    FASHION = "fashion"
    FOOD = "food"
    
    @classmethod
    def get_all(cls):
        return [
            cls.ELECTRONICS,
            cls.FURNITURE,
            cls.AUTO_PARTS,
            cls.FASHION,
            cls.FOOD
        ]