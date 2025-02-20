# seed.py
from app import create_app
from global_db_object import db
from werkzeug.security import generate_password_hash
from models.UserModel import User
from models.ElectronicModel import Electronic
from models.Category import ProductCategory

app = create_app()

with app.app_context():
    db.drop_all()  
    db.create_all()
    print("Created tables in: ", db.engine.url, db.engine.dialect.name)
    print("Tables: ", db.metadata.tables.keys())

    # Seed the data
    admin = User()
    admin.username = "admin"
    admin.password_hash = generate_password_hash("admin123")
    admin.role = "admin"
    db.session.add(admin)

    # Seed Electronics
    laptop = Electronic()
    laptop.name = "MacBook Pro"
    laptop.description = "Powerful laptop for professionals"
    laptop.specification = "Latest model with M2 chip"
    laptop.price = 1299.99
    laptop.stock = 10
    laptop.power_rating = 100
    laptop.battery_life = 20
    laptop.energy_efficiency_rating = "A+"
    laptop.manufacturer = "Apple"
    laptop.warranty_period = 12
    laptop.dimensions = "30.41 x 21.24 x 1.56 cm"
    laptop.weight = "1.4 kg"
    laptop.operating_system = "macOS"
    laptop.processor = "M2"
    laptop.ram = "16GB"
    laptop.storage = "512GB SSD"
    db.session.add(laptop)

    phone = Electronic()
    phone.name = "iPhone 15"
    phone.description = "Latest iPhone model"
    phone.specification = "Pro Max version"
    phone.price = 999.99
    phone.stock = 15
    phone.power_rating = 20
    phone.battery_life = 24
    phone.energy_efficiency_rating = "A"
    phone.manufacturer = "Apple"
    phone.warranty_period = 12
    phone.dimensions = "15.99 x 7.19 x 0.83 cm"
    phone.weight = "0.221 kg"
    phone.operating_system = "iOS"
    phone.processor = "A17 Pro"
    phone.ram = "8GB"
    phone.storage = "256GB"
    db.session.add(phone)

    # Commit all changes
    db.session.commit()
    
    print("Database seeded successfully!")
    print(f"Created tables in: {db.engine.url}")
    print(f"Tables: {db.metadata.tables.keys()}")
