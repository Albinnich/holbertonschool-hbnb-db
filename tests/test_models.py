import unittest
from app import app, db
from app.models import User
from app.data_manager import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.data_manager = DataManager()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_save_user(self):
        user = User(id='1', email='test@example.com', password='password123', is_admin=False)
        self.data_manager.save_user(user)
        retrieved_user = User.query.get('1')
        self.assertEqual(retrieved_user.email, 'test@example.com')

    def test_get_user_by_id(self):
        user = User(id='1', email='test@example.com', password='password123', is_admin=False)
        db.session.add(user)
        db.session.commit()
        retrieved_user = self.data_manager.get_user_by_id('1')
        self.assertEqual(retrieved_user.email, 'test@example.com')

    if __name__ == '__main__':
        unittest.main()
