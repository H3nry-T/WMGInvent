#test the InventoryService class 
import unittest
from app import create_app
from config import TestingConfig
from global_db_object import db
from services.ElectronicsService import ElectronicsService
from repositories.ElectronicsRepository import ElectronicsRepository
from models.ElectronicModel import Electronic

class TestInventoryService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(config_class=TestingConfig)
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.drop_all()
        cls.app_context.pop()

    def setUp(self):
        self.electronics_service = ElectronicsService(ElectronicsRepository(db))
        electronic = Electronic() 
        electronic.name="Iphone 16"
        electronic.description="Latest model with A17 Bionic chip"
        electronic.specification="Latest model with A17 Bionic chip"
        electronic.price=700
        electronic.stock=5
        electronic.power_rating=100
        electronic.battery_life=20
        electronic.energy_efficiency_rating="A+"
        electronic.manufacturer="Apple"
        electronic.warranty_period=12
        electronic.dimensions="30.41 x 21.24 x 1.56 cm"
        electronic.weight="1.4 kg"
        electronic.operating_system="IOS"
        electronic.processor="A17 Bionic chip"
        electronic.ram="8GB"
        electronic.storage="128GB"
        self.electronics_service.create_electronic(electronic)

    def tearDown(self):
        # clear data between tests
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()

    def test_create_electronic(self): 
        electronic = Electronic() 
        electronic.name="MacBook Pro"
        electronic.description="Powerful laptop for professionals"
        electronic.specification="Latest model with M2 chip"
        electronic.price=1299.99
        electronic.stock=10
        electronic.power_rating=100
        electronic.battery_life=20
        electronic.energy_efficiency_rating="A+"
        electronic.manufacturer="Apple"
        electronic.warranty_period=12
        electronic.dimensions="30.41 x 21.24 x 1.56 cm"
        electronic.weight="1.4 kg"
        electronic.operating_system="macOS"
        electronic.processor="M2"
        electronic.ram="16GB"
        electronic.storage="512GB SSD"
        self.electronics_service.create_electronic(electronic)
        self.assertEqual(electronic.id, 2)
        self.assertEqual(electronic.name, "MacBook Pro")
        self.assertEqual(electronic.description, "Powerful laptop for professionals")
        self.assertEqual(electronic.specification, "Latest model with M2 chip")
        self.assertEqual(electronic.price, 1299.99)
        self.assertEqual(electronic.stock, 10)
        self.assertEqual(electronic.power_rating, 100)
        self.assertEqual(electronic.battery_life, 20)
        self.assertEqual(electronic.energy_efficiency_rating, "A+")
        self.assertEqual(electronic.manufacturer, "Apple")
        self.assertEqual(electronic.warranty_period, 12)
        self.assertEqual(electronic.dimensions, "30.41 x 21.24 x 1.56 cm")
        self.assertEqual(electronic.weight, "1.4 kg")
        self.assertEqual(electronic.operating_system, "macOS")
        self.assertEqual(electronic.processor, "M2")
        self.assertEqual(electronic.ram, "16GB")
        self.assertEqual(electronic.storage, "512GB SSD")

    def test_get_all_electronics(self):
        electronics = self.electronics_service.get_all_electronics()
        self.assertEqual(len(electronics), 1)