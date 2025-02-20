from global_db_object import db
from models.Category import ProductCategory
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    specification = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50))  # Discriminator
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    image = db.Column(db.String(255), nullable=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'products',
        'polymorphic_on': category
    }



