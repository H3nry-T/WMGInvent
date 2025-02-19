import unittest
from app import create_app, db
from config import TestingConfig
from models.UserModel import User
from werkzeug.security import generate_password_hash, check_password_hash

class AuthTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(config_class=TestingConfig)
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()
        cls.client = cls.app.test_client()

    @classmethod
    def tearDownClass(cls):
        db.drop_all()
        cls.app_context.pop()

    def test_successful_register(self):
        """test register and check if user is in DB"""
        response = self.client.post(
            "/register",
            data={
                "username": "testregister",
                "password": "testpassword",
                "confirm_password": "testpassword",
                "role": "admin"
            },
            follow_redirects=True
        )
        self.assertIn(b"Registration successful", response.data)

        user: User | None = User.query.filter_by(username="testregister").first()
        self.assertIsNotNone(user)
        if user: 
            self.assertEqual(user.username, "testregister")
            self.assertTrue(check_password_hash(user.password_hash, "testpassword"))
            self.assertEqual(user.role, "admin")
        else: 
            self.fail("User not found in DB")

    def test_failed_register(self):
        """test register with duplicate username"""
        response = self.client.post(
            "/register",
            data={
                "username": "testrepeat",
                "password": "testpassword",
                "confirm_password": "testpassword",
                "role": "manager"
            },
            follow_redirects=False
        )
        response = self.client.post(
            "/register",
            data={
                "username": "testrepeat",
                "password": "testpassword",
                "confirm_password": "testpassword",
                "role": "manager"
            },
            follow_redirects=True
        )
        # Check if the user already exists
        self.assertIn(b"Username already exists", response.data)

    def test_login(self):
        """test login and check redirect to electronics browse page"""
        self.client.post(
            "/register",
            data={
                "username": "testlogin",
                "password": "test12345",
                "confirm_password": "test12345",
                "role": "manager"
            },
            follow_redirects=True
        )

        # login
        response = self.client.post(
            "/login",
            data={
                "username": "testlogin",
                "password": "test12345",
            },
            follow_redirects=True
        )
        self.assertNotIn(b"Invalid username or password", response.data)
        # check if we see electronics browse page
        self.assertIn(b"Browse Products", response.data)

    def test_logout(self):
        """test logout and check redirect to login page"""
        self.client.post(
            "/register",
            data={
                "username": "testlogout",
                "password": "logoutpass",
                "confirm_password": "logoutpass",
                "role": "manager"
            },
            follow_redirects=True
        )
        self.client.post(
            "/login",
            data={
                "username": "testlogout",
                "password": "logoutpass"
            },
            follow_redirects=True
        )

        response = self.client.get("/logout", follow_redirects=True)

        self.assertIn(b"Sign in to your account", response.data)

if __name__ == '__main__':
    unittest.main()
