
import unittest
from app import create_app, db
from config import TestingConfig
from models.UserModel import User
from werkzeug.security import generate_password_hash
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
        """Run once after all tests."""
        db.drop_all()
        cls.app_context.pop()

    def test_register(self):
        """Test user registration flow."""
        response = self.client.post(
            "/register",
            data={
                "username": "testuser",
                "password": "testpassword",
                "confirm_password": "testpassword"
            },
            follow_redirects=True
        )
        self.assertIn(b"Registration successful", response.data)

        # Verify user in DB with credentials
        user: User | None = User.query.filter_by(username="testuser").first()
        self.assertIsNotNone(user)
        if user: 
            self.assertEqual(user.username, "testuser")
            reverse_password_hash = generate_password_hash("testpassword")
            self.assertTrue(user.password_hash, reverse_password_hash)
        else: 
            self.fail("User not found in DB")

    def test_login(self):
        """Test user login flow."""
        # 1) Register a user
        self.client.post(
            "/register",
            data={
                "username": "testlogin",
                "password": "test12345",
                "confirm_password": "test12345"
            },
            follow_redirects=True
        )

        # 2) Attempt login
        response = self.client.post(
            "/login",
            data={
                "username": "testlogin",
                "password": "test12345"
            },
            follow_redirects=True
        )
        self.assertNotIn(b"Invalid username or password", response.data)
        # Possibly check if we see some home page text
        self.assertIn(b"Browse Products", response.data)

    def test_logout(self):
        """Test user logout flow."""
        # Register and login user
        self.client.post(
            "/register",
            data={
                "username": "testlogout",
                "password": "logoutpass",
                "confirm_password": "logoutpass"
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

        # Now logout
        response = self.client.get("/logout", follow_redirects=True)
        # Check if we see "Sign in" or "Login" text, meaning we are redirected to login
        self.assertIn(b"Sign in to your account", response.data)

if __name__ == '__main__':
    unittest.main()
