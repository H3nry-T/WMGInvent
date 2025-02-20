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
    laptop.image = "images/macbook.jpeg"
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
    phone.image = "images/iphone.jpeg"
    db.session.add(phone)

    headphone = Electronic()
    headphone.name = "Sony WH-1000XM4"
    headphone.description = "Noise-cancelling headphones"
    headphone.specification = "Advanced noise cancellation"
    headphone.price = 399.99
    headphone.stock = 1
    headphone.power_rating = 10
    headphone.battery_life = 20
    headphone.energy_efficiency_rating = "A+"
    headphone.manufacturer = "Sony"
    headphone.warranty_period = 12
    headphone.dimensions = "30.41 x 21.24 x 1.56 cm"
    headphone.weight = "500g"
    headphone.operating_system = "Android"
    headphone.processor = "Snapdragon 865"
    headphone.ram = "8GB"
    headphone.storage = "256GB"
    headphone.image = "images/headphones.jpeg"
    db.session.add(headphone)
    
    airpods = Electronic()
    airpods.name = "Apple AirPods Pro"
    airpods.description = "Wireless earbuds with active noise cancellation"
    airpods.specification = "Active noise cancellation and spatial audio"
    airpods.price = 249.99
    airpods.stock = 15
    airpods.power_rating = 10
    airpods.battery_life = 20
    airpods.energy_efficiency_rating = "A+"
    airpods.manufacturer = "Apple"
    airpods.warranty_period = 12
    airpods.dimensions = "30.41 x 21.24 x 1.56 cm"
    airpods.weight = "500g"
    airpods.operating_system = "iOS"
    airpods.processor = "H1 chip"
    airpods.ram = "1GB"
    airpods.storage = "16GB"
    airpods.image = "images/airpods.jpeg"
    db.session.add(airpods)

    dell_desktop = Electronic()
    dell_desktop.name = "Dell Inspiron 3050"
    dell_desktop.description = "Powerful desktop for professionals"
    dell_desktop.specification = "Latest model with Intel Core i5"
    dell_desktop.price = 599.99
    dell_desktop.stock = 0
    dell_desktop.power_rating = 100
    dell_desktop.battery_life = 20
    dell_desktop.energy_efficiency_rating = "A+"
    dell_desktop.manufacturer = "Dell"
    dell_desktop.warranty_period = 12
    dell_desktop.dimensions = "30.41 x 21.24 x 1.56 cm"
    dell_desktop.weight = "1.4 kg"
    dell_desktop.operating_system = "Windows 10"
    dell_desktop.processor = "Intel Core i5"
    dell_desktop.ram = "8GB"
    dell_desktop.storage = "256GB SSD"
    dell_desktop.image = "images/desktop.jpeg"
    db.session.add(dell_desktop)

    dell_laptop = Electronic() 
    dell_laptop.name = "Dell Inspiron 3510"
    dell_laptop.description = "Modern laptop with high performance and battery life"
    dell_laptop.specification = "Latest model with Intel Core i9"
    dell_laptop.price = 1299.99
    dell_laptop.stock = 150
    dell_laptop.power_rating = 150
    dell_laptop.battery_life = 9
    dell_laptop.energy_efficiency_rating = "B+"
    dell_laptop.manufacturer = "Dell"
    dell_laptop.warranty_period = 12
    dell_laptop.dimensions = "30.41 x 21.24 x 1.56 cm"
    dell_laptop.weight = "1.2kg"
    dell_laptop.operating_system = "Windows 11"
    dell_laptop.processor = "Intel Core i9"
    dell_laptop.ram = "32GB"
    dell_laptop.storage = "1TB HDD"
    dell_laptop.image = "images/laptop.jpeg"
    db.session.add(dell_laptop)

    light_bulb = Electronic() 
    light_bulb.name = "Philips LED Light Bulb"
    light_bulb.description = "Energy-efficient LED light bulb"
    light_bulb.specification = "Latest model with 2000 lumens"
    light_bulb.price = 19.99
    light_bulb.stock = 100
    light_bulb.power_rating = 10
    light_bulb.manufacturer = "Philips"
    light_bulb.warranty_period = 12
    light_bulb.dimensions = "10 x 10 x 10 cm"
    light_bulb.weight = "0.1kg"
    light_bulb.image = "images/lightbulb.jpeg"
    db.session.add(light_bulb)

    usb_c_cable = Electronic()
    usb_c_cable.name = "USB C Cable"
    usb_c_cable.description = "USB C cable for charging and data transfer"
    usb_c_cable.specification = "Latest model with USB C"
    usb_c_cable.price = 19.99
    usb_c_cable.stock = 100
    usb_c_cable.power_rating = 10
    usb_c_cable.manufacturer = "Apple"
    usb_c_cable.warranty_period = 12
    usb_c_cable.dimensions = "1 x 1 x 100 cm"
    usb_c_cable.weight = "0.1kg"
    usb_c_cable.image = "images/usb_c.jpeg"
    db.session.add(usb_c_cable)
    
    # Commit all changes
    db.session.commit()
    
    print("Database seeded successfully!")
    print(f"Created tables in: {db.engine.url}")
    print(f"Tables: {db.metadata.tables.keys()}")
