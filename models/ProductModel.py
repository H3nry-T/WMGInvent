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
    # Polymorphic
    __mapper_args__ = {
        'polymorphic_identity': ProductCategory.ELECTRONICS,
        'polymorphic_on': category
    }



