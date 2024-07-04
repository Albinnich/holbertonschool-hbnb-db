import unittest
from models.engine.db_storage import DBStorage
from models.user import User

class TestDBStorage(unittest.TestCase):
    def setUp(self):
        self.db = DBStorage()

    def test_save_user(self):
        user_data = {
            'email': 'test@example.com',
            'password': 'password123',
            'is_admin': False
        }
        user = User(**user_data)
        self.db.save_user(user)

        retrieved_user = self.db.get_user(user.id)
        self.assertEqual(user.email, retrieved_user.email)

if __name__ == '__main__':
    unittest.main()
