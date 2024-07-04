import unittest
from models.user import User
from models.engine import db_storage

class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'password': 'password123',
            'is_admin': False
        }

    def test_create_user(self):
        # Test creating a user instance
        user = User(**self.user_data)
        db_storage.DBStorage().save_user(user)
        self.assertIsNotNone(user.id)

    def test_get_user(self):

        user = User(**self.user_data)
        db_storage.DBStorage().save_user(user)
        
        retrieved_user = db_storage.DBStorage().get_user(user.id)
        self.assertEqual(user.email, retrieved_user.email)

if __name__ == '__main__':
    unittest.main()
