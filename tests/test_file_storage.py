import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def test_save_user(self):
        user_data = {
            'id': 'test_id',
            'email': 'test@example.com',
            'password': 'password123',
            'is_admin': False
        }
        self.file_storage.save_user(user_data)

        retrieved_user = self.file_storage.get_user('test_id')
        self.assertEqual(user_data['email'], retrieved_user['email'])

if __name__ == '__main__':
    unittest.main()
