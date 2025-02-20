from models.ProductModel import Product
from models.Category import ProductCategory
from global_db_object import db
from typing import Optional
class Electronic(Product):
    __tablename__ = 'electronics'
    id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    power_rating = db.Column(db.Integer)
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

    #for debugging prints
    def __repr__(self):
        return f'<Electronic {self.name}>'
    
    def json(self): 
        """transforms the ElectronicModel into a json format"""
        return {
            'id': self.id,
            'name': self.name, 
            'description' : self.description,
            'specification': self.specification,
            'category' : self.category,
            'price' : self.price,
            'stock': self.stock,
            'power_rating': self.power_rating,
            'battery_life': self.battery_life,
            'energy_efficiency_rating': self.energy_efficiency_rating,
            'manufacturer': self.manufacturer,
            'warranty_period': self.warranty_period,
            'dimensions': self.dimensions,
            'weight': self.weight,
            'operating_system': self.operating_system,
            'processor': self.processor,
            'ram': self.ram,
            'storage': self.storage,
        }