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
        self.assertEqual(electronics[0].name, "Iphone 16")
        self.assertEqual(electronics[0].description, "Latest model with A17 Bionic chip")
        self.assertEqual(electronics[0].specification, "Latest model with A17 Bionic chip")
        self.assertEqual(electronics[0].price, 700)
        self.assertEqual(electronics[0].stock, 5)

    def test_get_electronics_by_id(self):
        
        electronic = self.electronics_service.get_electronics_by_id(1)
        self.assertIsNotNone(electronic)
        if electronic: 
            self.assertEqual(electronic.name, "Iphone 16")
            self.assertEqual(electronic.manufacturer, "Apple")
        
        
        non_existent = self.electronics_service.get_electronics_by_id(999)
        self.assertIsNone(non_existent)

    def test_update_electronics_by_id(self):
        
        updates = {
            "price": 800,
            "stock": 10,
            "ram": "32GB"
        }
        
        original = self.electronics_service.get_electronics_by_id(1)
        if original: 
            self.assertIsNotNone(original)
            self.assertEqual(original.price, 700)  
        
        updated_electronic = self.electronics_service.update_electronics_by_id(1, updates)
        if updated_electronic: 
            self.assertIsNotNone(updated_electronic)
            self.assertEqual(updated_electronic.price, 800)
            self.assertEqual(updated_electronic.stock, 10)
            self.assertEqual(updated_electronic.ram, "32GB")
        
        refreshed = self.electronics_service.get_electronics_by_id(1)
        if refreshed: 
            self.assertEqual(refreshed.price, 800)
            self.assertEqual(refreshed.stock, 10)
            self.assertEqual(refreshed.ram, "32GB")
        
        non_existent = self.electronics_service.update_electronics_by_id(999, updates)
        self.assertIsNone(non_existent)
        
        invalid_updates = {
            "invalid_field": "value",
            "price": 900
        }
        updated_electronic = self.electronics_service.update_electronics_by_id(1, invalid_updates)
        if updated_electronic: 
            self.assertIsNotNone(updated_electronic)
            self.assertEqual(updated_electronic.price, 900)  
        self.assertFalse(hasattr(updated_electronic, "invalid_field"))  

    def test_count_electronics(self):
        count = self.electronics_service.count_electronics()
        self.assertEqual(count, 1)
        
        
        electronic = Electronic()
        electronic.name = "Test Device"
        electronic.description = "Test Description"
        electronic.specification = "Test Specs"
        electronic.price = 100
        electronic.stock = 1
        electronic.manufacturer = "Test Manufacturer"
        electronic.warranty_period = 12
        electronic.dimensions = "10 x 10 x 10"
        electronic.weight = "1kg"
        self.electronics_service.create_electronic(electronic)
        
        new_count = self.electronics_service.count_electronics()
        self.assertEqual(new_count, 2)

    def test_search_electronics(self):
        
        results = self.electronics_service.search_electronics(keyword="iPhone")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Iphone 16")

        
        results = self.electronics_service.search_electronics(
            keyword="",
            min_price=600,
            max_price=800
        )
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].price, 700)

        
        results = self.electronics_service.search_electronics(
            keyword="NonExistent"
        )
        self.assertEqual(len(results), 0)

        
        results = self.electronics_service.search_electronics(
            keyword="",
            stock_status="low_stock"  
        )
        self.assertEqual(len(results), 1)
        self.assertTrue(all(e.stock <= 5 for e in results))

    def test_delete_electronic(self):
        
        electronic = self.electronics_service.get_electronics_by_id(1)
        self.assertIsNotNone(electronic)
        
        
        if electronic: 
            deleted = self.electronics_service.delete_electronic(electronic)
            self.assertTrue(deleted)
            
            
            electronic = self.electronics_service.get_electronics_by_id(1)
            self.assertIsNone(electronic)
            
            
        count = self.electronics_service.count_electronics()
        self.assertEqual(count, 0)

    def test_update_electronic(self):
        
        electronic = self.electronics_service.get_electronics_by_id(1)
        
        if electronic: 
            electronic.price = 750
            electronic.stock = 15
            electronic.ram = "16GB"
            
            
            updated = self.electronics_service.update_electronic(electronic)
            self.assertIsNotNone(updated)
            
            
        refreshed = self.electronics_service.get_electronics_by_id(1)
        if refreshed: 
            self.assertEqual(refreshed.price, 750)
            self.assertEqual(refreshed.stock, 15)
            self.assertEqual(refreshed.ram, "16GB")

    def test_search_electronics_edge_cases(self):
        
        results = self.electronics_service.search_electronics(
            keyword="",
            min_price=None,
            max_price=None,
            stock_status=None
        )
        self.assertEqual(len(results), 1)  

        
        results = self.electronics_service.search_electronics(
            keyword="",
            min_price=1000,
            max_price=500  
        )
        self.assertEqual(len(results), 0)

        
        results = self.electronics_service.search_electronics(
            keyword="",
            min_price=0,
            max_price=10000
        )
        self.assertEqual(len(results), 1)  

    