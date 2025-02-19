from models.ProductModel import Product
from models.Category import ProductCategory
from global_db_object import db

class Electronic(Product):
    __tablename__ = 'electronics'
    id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    power_rating = db.Column(db.Integer, nullable=False)
    battery_life = db.Column(db.Integer)
    energy_efficiency_rating = db.Column(db.String(50))
    manufacturer = db.Column(db.String(100), nullable=False)
    warranty_period = db.Column(db.Integer, nullable=False)
    dimensions = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.String(50), nullable=False)
    operating_system = db.Column(db.String(100))
    processor = db.Column(db.String(100))
    ram = db.Column(db.String(50))
    storage = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': ProductCategory.ELECTRONICS,
    }

    def __repr__(self):
        return f'<Electronic {self.name}>'